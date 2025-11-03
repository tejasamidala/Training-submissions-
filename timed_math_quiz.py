import random
import time

def quiz_timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"\n⏱ Time taken: {round(end - start, 2)} seconds")
    return wrapper

@quiz_timer
def math_quiz():
    print("🎯 Welcome to the Timed Math Quiz!")
    score = 0
    for i in range(5):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*"])
        correct = eval(f"{num1} {operation} {num2}")
        answer = int(input(f"Q{i+1}: {num1} {operation} {num2} = "))
        if answer == correct:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The right answer was {correct}")
    print(f"\n🏁 Final Score: {score}/5")

math_quiz()