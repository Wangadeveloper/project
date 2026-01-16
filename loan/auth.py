from flask_login import UserMixin
from loan.repositories.user_repo import UserRepository
from loan import login_manager
from loan.repositories.profile_repo import ProfileRepository

class LoginUser:
    def __init__(self, row):
        self.id = row["id"]
        self.username = row["username"]
        self.email = row["email"]
        # Load profile if it exists
        profile_row = ProfileRepository.get_by_user_id(self.id)
        if profile_row:
            self.profile = profile_row
            # Optionally, expose fields directly
            self.full_names = profile_row.get("full_names")
            self.monthly_income = profile_row.get("monthly_income")
            self.business_type = profile_row.get("business_type")
            self.business_level = profile_row.get("business_level")
            self.phone = profile_row.get("phone")
            self.country = profile_row.get("country")
            self.location = profile_row.get("location")
        else:
            self.profile = None

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


@login_manager.user_loader
def load_user(user_id):
    row = UserRepository.get_by_id(int(user_id))
    return LoginUser(row) if row else None

