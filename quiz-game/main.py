from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(text = question["text"], answer = question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions() == True:
    quiz.next_question()

print("You have completed the challenge!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")