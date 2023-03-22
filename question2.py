import random

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) London", "B) Paris", "C) Rome"],
        "answer": "B"
    },
    {
        "question": "What is the largest organ in the human body?",
        "choices": ["A) Heart", "B) Liver", "C) Skin"],
        "answer": "C"
    },
    {
        "question": "Who wrote the book '1984'?",
        "choices": ["A) George Orwell", "B) J.K. Rowling", "C) Charles Dickens"],
        "answer": "A"
    }
]

# Shuffle the quiz questions
random.shuffle(questions)

# Initialize the quiz score
score = 0

# Loop through each question and ask the user
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for choice in q['choices']:
        print(choice)
    answer = input("Enter your answer (A, B, or C): ")
    if answer.upper() == q['answer']:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

# Print the final quiz results
print(f"\nQuiz complete! You scored {score} out of {len(questions)}")
