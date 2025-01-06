import os
from dotenv import load_dotenv
import openai

# Cargar variables de entorno
load_dotenv()

# Configuración de la clave de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_claim(claim: str):
    """
    Usa OpenAI para analizar una afirmación.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # También puedes usar "gpt-3.5-turbo" si es necesario
            messages=[
                {"role": "system", "content": "You are an expert in health and nutrition."},
                {"role": "user", "content": f"Please verify the following claim: '{claim}'. Provide references if possible."},
            ],
            temperature=0.7,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {e}"
