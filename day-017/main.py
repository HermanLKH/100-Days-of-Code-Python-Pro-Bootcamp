# TODO 2. create question bank list contains questions objects initiated by question data
# write a for loop to iterate over the question_data
# create a Question object from each entry in question_data
# append each Question object to the question_bank
# TODO 8. print a complete message and the user's final score
# TODO 9. get new questions from Trivia
# change the name of the keys to get the correct data


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question()
else:
    print("You've completed the quiz!")
    print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}.")
