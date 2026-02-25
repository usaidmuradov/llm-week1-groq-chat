# LLM Week 1 – Groq bilan oddiy konsol chatbot

Bu loyiha **Groq LLM API**’dan foydalanib, konsolda ishlaydigan oddiy chat dasturini yaratish uchun mo‘ljallangan.  
Maqsad – API kaliti, `.env` fayli, virtual environment va modulga bo‘lingan Python loyihasi bilan tanishish.

---

## 🛠 Texnologiyalar

* **Python 3.10+**
* **[Groq](https://groq.com/)** – LLM API
* **`groq`** – Python kutubxonasi
* **`python-dotenv`** – `.env` fayldan API kalitni o‘qish uchun

---

## 📂 Loyiha tuzilmasi

```text
llm-week1/
├─ .venv/          # Virtual environment (GitHub’ga qo‘yilmaydi)
├─ .env            # GROQ_API_KEY shu yerda (maxfiy)
├─ requirements.txt
├─ llm_client.py   # Groq bilan ishlaydigan modul
├─ main.py         # Konsol chat dasturi
└─ README.md
🚀 O‘rnatish
Repozitoriyani kompyuteringizga yuklang va papkaga kiring:

Bash
cd llm-week1
Virtual environment yarating va yoqing:

Windows uchun:

Bash
python -m venv .venv
.venv\Scripts\activate
Linux/macOS uchun:

Bash
python3 -m venv .venv
source .venv/bin/activate
Kerakli kutubxonalarni o‘rnating:

Bash
pip install -r requirements.txt
.env faylini yarating va Groq API kalitingizni kiriting:

Plaintext
GROQ_API_KEY=BU_YERGA_SIZNING_GROQ_API_KEYINGIZ
🎮 Ishga tushirish
Virtual environment aktiv bo‘lgan holda quyidagi buyruqni bering:

Bash
python main.py
Foydalanish tartibi:

Siz: degan joyga savolingizni yozing.

Javob AI: prefiksi bilan chiqadi.

Dasturdan chiqish uchun exit yoki quit deb yozing.

⚙️ Qisqacha qanday ishlaydi?
llm_client.py: .env fayldan GROQ_API_KEY ni o‘qiydi, Groq klientini yaratadi va ask_llm(prompt) funksiyasi orqali savolni LLM modeliga yuborib, matnli javobni qaytaradi.

main.py: Foydalanuvchidan input() orqali matn oladi, uni ask_llm funksiyasiga beradi va qaytgan javobni konsolga chiqaradi.

Bu loyiha LLM va API bilan ishlashni amalda o‘rganish uchun birinchi oddiy qadam sifatida yaratilgan.
