from llm_client import ask_llm

def main():
    print("LLM chatga xush kelibsiz! Chiqish uchun 'exit' yozing.\n")
    while True:
        user_input = input("Siz: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Chiqildi.")
            break

        try:
            answer = ask_llm(user_input)
            print(f"AI: {answer}\n")
        except Exception as e:
            print(f"Xato yuz berdi: {e}")

if __name__ == "__main__":
    main()