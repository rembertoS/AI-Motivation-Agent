from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_motivational_quote():
    prompt = (
        "Generate a short, unique motivational quote. "
        "No clichés. Keep it under 25 words. "
        "Tone: uplifting, positive, and encouraging."
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You generate high-quality motivational quotes"} , 
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


