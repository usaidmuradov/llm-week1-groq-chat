LLM Week 1 – Groq bilan oddiy konsol chatbot
Bu loyiha Groq LLM API’dan foydalanib, kompyuter konsolida ishlaydigan oddiy chat dasturini yaratish uchun tuzilgan.
Asosiy maqsad – API kalitlari, .env fayli, virtual environment va modulga bo‘lingan oddiy Python loyihasi bilan tanishish.
Texnologiyalar
Python 3.10 yoki undan yuqori
Groq LLM API
groq Python kutubxonasi
python-dotenv kutubxonasi (.env fayldan API kalitini o‘qish uchun)
Loyiha tuzilmasi
llm-week1 papkasi quyidagi asosiy fayllardan iborat:
llm_client.py – Groq bilan ishlaydigan modul, LLM’dan javob olish funksiyasi shu yerda
main.py – foydalanuvchi bilan konsol orqali suhbat qiladigan dastur
requirements.txt – kerakli Python kutubxonalar ro‘yxati
README.md – ushbu hujjat
Eslatma: .env faylida GROQ_API_KEY saqlanadi va u maxfiy fayl, GitHub yoki boshqalarga ulashilmaydi.
O‘rnatish
Quyidagi qadamlar yangi kompyuterda loyihani ishga tushirish uchun yetarli:
1) Loyiha fayllarini kompyuteringizga yuklab oling (masalan, GitHub’dan clone yoki zip).
2) Terminal yoki PowerShell oynasida loyiha papkasiga kiring.
Masalan:
cd llm-week1
3) Virtual environment yarating va yoqing (ixtiyoriy, lekin tavsiya etiladi):
python -m venv .venv
Windows’da:
.venv\Scripts\activate
4) Kerakli kutubxonalarni o‘rnating:
pip install -r requirements.txt
5) Loyiha papkasida .env nomli fayl yarating va ichiga quyidagicha qatordan iborat ma’lumot yozing:
GROQ_API_KEY=SIZNING_GROQ_API_KEYINGIZ
Bu yerga o‘zingizning haqiqiy Groq API kalitingizni yozasiz.
Dasturdan foydalanish
1) Virtual environment aktiv bo‘lgan holatda loyiha papkasida quyidagi buyruqni bajaring:
python main.py
2) Konsolda quyidagiga o‘xshash xabar chiqadi:
LLM chatga xush kelibsiz! Chiqish uchun 'exit' yozing.
3) “Siz:” qatorida savolingizni yozing va Enter bosing.
Misol:
Machine learning va deep learning o‘rtasidagi farq nima?
4) Modeldan javob keladi va “AI:” prefiksi bilan konsolda ko‘rinadi.
5) Dasturdan chiqish uchun “exit” yoki “quit” so‘zini kiriting va Enter bosing.
Qisqacha ichki ishlash prinsipi
llm_client.py faylida:
.env fayldan GROQ_API_KEY o‘qiladi.
Shu kalit yordamida Groq klienti yaratiladi.
ask_llm(prompt) funksiyasi foydalanuvchi matnini Groq LLM modeliga yuboradi va qaytgan javobni oddiy matn sifatida qaytaradi.
main.py faylida:
dastur foydalanuvchidan input funksiyasi orqali matn oladi;
bu matnni ask_llm funksiyasiga uzatadi;
olingan javobni ekranga chiqaradi;
foydalanuvchi “exit” yoki “quit” yozguncha sikl davom etadi.
Bu kichik loyiha LLM va API bilan ishlashni amaliy misol orqali o‘rganish uchun mo‘ljallangan birinchi bosqich hisoblanadi.

