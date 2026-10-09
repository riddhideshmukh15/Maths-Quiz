score = 0

questions = [
    ("5+7", 12),
    ("56+90", 146),
    ("20/5", 4),
    ("769/3", 769/3),
    ("9+8", 17)
]

while True:
    score = 0

    print("\n==== Math Quiz ====")
    name = input("Enter your name: ")

    for question, answer in questions:
        print("\nWhat is", question, "?")
        user_answer = float(input("Your answer: "))

        if abs(user_answer - answer) < 0.01:
            print("Correct!")
            score += 1
        else:
            print("Wrong! Correct answer:", round(answer, 2))

    percentage = (score / len(questions)) * 100

    print("\n==== Quiz Result ====")
    print("Name:", name)
    print("Your Score:", score, "/", len(questions))
    print("Percentage:", round(percentage, 2), "%")

    if percentage >= 80:
        print("Grade: Excellent!")
    elif percentage >= 60:
        print("Grade: Good!")
    elif percentage >= 40:
        print("Grade: Average")
    else:
        print("Grade: Keep Practicing!")

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for playing!")
        break
