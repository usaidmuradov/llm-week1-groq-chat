import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY .env faylda topilmadi")

client = Groq(api_key=GROQ_API_KEY)

def ask_llm(prompt: str) -> str:
    chat_completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "Siz foydalanuvchiga qisqa, aniq va takrorlanmas javob beradigan yordamchi AI assitentsiz."
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )
    return chat_completion.choices[0].message.content