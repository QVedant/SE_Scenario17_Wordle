from game import WordleGame

if __name__ == "__main__":
    while True:
        choice = input("Choose word length (4, 5, or 6): ").strip()

        if choice in ("4", "5", "6"):
            WordleGame(length=int(choice)).run()
            break

        print("Invalid choice. Enter 4, 5, or 6.")
