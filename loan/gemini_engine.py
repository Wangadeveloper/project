
import os
from io import BytesIO
import google.generativeai as genai
from fpdf import FPDF
from flask import current_app

def generate_pdf(content: str, title: str = "AI Advice") -> BytesIO:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, title, ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    # Strip or replace emojis (non-ASCII chars)
    cleaned_content = content.encode("ascii", "ignore").decode()
    pdf.multi_cell(0, 8, cleaned_content)

    pdf_output = BytesIO()
    pdf_output.write(pdf.output(dest="S").encode("latin1", errors="replace"))
    pdf_output.seek(0)
    return pdf_output



def get_model(model_name="gemini-1.5-flash"):
    # Get API key from Flask config or env
    api_key = current_app.config.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError("❌ GOOGLE_API_KEY is not set")

    import google.generativeai as genai
    genai.configure(api_key=api_key)

    generation_config = {
        "temperature": 0.3,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        # "response_mime_type": "text/plain",  <-- REMOVE THIS
    }

    return genai.GenerativeModel(model_name=model_name, generation_config=generation_config)


# 🔹 Financial Advice (return TEXT, not PDF)
def get_financial_advice(farm_data: str) -> str:
    try:
        prompt = f"""
        You are a financial advisor.
        Given this bussiness situation:
        {farm_data}

        Provide simple, clear advice on:
        - Revenue optimization
        - Investment opportunities
        - Risk management
        """
        model = get_model("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error generating financial advice: {str(e)}"

