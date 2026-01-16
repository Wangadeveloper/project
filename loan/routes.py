from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from loan.forms import RegistrationForm, LoginForm ,LoanRiskAssessmentForm
from loan.repositories.user_repo import UserRepository
from loan.auth import LoginUser
from loan import bcrypt
import uuid
import os
import re
import os
from fpdf import FPDF
from io import BytesIO
from loan.gemini_engine import * # Import Gemini functions
import markdown as md

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")


@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = RegistrationForm()

    if form.validate_on_submit():
        if UserRepository.get_by_email(form.email.data):
            flash("Email already registered.", "danger")
            return redirect(url_for("main.register"))

        password_hash = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        UserRepository.create(
            username=form.username.data,
            email=form.email.data,
            password_hash=password_hash
        )

        flash("Account created. Please log in.", "success")
        return redirect(url_for("main.login"))

    return render_template("register.html", form=form)


@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))

    form = LoginForm()

    if form.validate_on_submit():
        row = UserRepository.get_by_email(form.email.data)

        if row and bcrypt.check_password_hash(
            row["password"], form.password.data
        ):
            login_user(LoginUser(row))
            return redirect(url_for("main.dashboard"))

        flash("Invalid credentials.", "danger")

    return render_template("login.html", form=form)


@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))


@main.route("/dashboard")
def dashboard():
    return render_template("account_info.html")

from loan.repositories.profile_repo import ProfileRepository
from loan.forms import UserProfileForm

@main.route("/profile", methods=["GET", "POST"])
def profile():
    form = UserProfileForm()

    existing_profile = ProfileRepository.get_by_user_id(
        current_user.id
    )

    if form.validate_on_submit():
        profile_data = {
            "full_names": form.full_names.data,
            "monthly_income": form.monthly_income.data,
            "business_type": form.business_type.data,
            "business_level": form.business_level.data,
            "phone": form.phone.data,
            "country": form.country.data,
            "location": form.location.data,
        }

        if existing_profile:
            ProfileRepository.update(
                current_user.id, profile_data
            )
            flash("Profile updated successfully!", "success")
        else:
            ProfileRepository.create(
                current_user.id, profile_data
            )
            flash("Profile created successfully!", "success")

        return redirect(url_for("main.dashboard"))

    # Pre-fill form on GET if profile exists
    if existing_profile:
        form.full_names.data = existing_profile["full_names"]
        form.monthly_income.data = existing_profile["monthly_income"]
        form.business_type.data = existing_profile["business_type"]
        form.business_level.data = existing_profile["business_level"]
        form.phone.data = existing_profile["phone"]
        form.country.data = existing_profile["country"]
        form.location.data = existing_profile["location"]

    return render_template("profile.html", form=form)

@main.route('/user_account')
def user_account():
    return render_template('account_info.html')

@main.route('/account')
def account():
    return render_template("account.html")

@main.route("/loan-risk-assessment", methods=["GET", "POST"])
def loan_risk_assessment():
    form = LoanRiskAssessmentForm()

    if form.validate_on_submit():
        query = f"""Give financial advice in English on what amount of
                    loan to apply in Kenya having a monthly
                    income of KES {form.monthly_income.data},
                    and a {form.business_type.data} business at a
                    {form.business_level.data} level with a repayment period
                    of {form.repayment_period.data} months.
                    Business description: {form.business_desc.data}"""

        eng_text = get_financial_advice(query)

        # ✅ Generate unique filename
        filename = f"advice_{uuid.uuid4().hex}.pdf"
        filepath = os.path.join(current_app.root_path, "static/reports", filename)

        # ✅ Save PDF instead of streaming
        with open(filepath, "wb") as f:
            pdf_bytes = generate_pdf(eng_text, title="Financial Advice Report")
            f.write(pdf_bytes.read())

        # ✅ Pass filename to template so user can download
        return render_template("loan-risk-assessment.html", form=form, advice_file=filename)

    return render_template("loan-risk-assessment.html", form=form)
