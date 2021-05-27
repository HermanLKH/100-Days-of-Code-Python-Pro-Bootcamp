# TODO 3. Create and setup QuizBrain
# create a class called QuizBrain
# write an __init__() method
# initialize the question_number = 0
# initialize the question_list to an input
# TODO 4. asking the questions
# retrieve the item at the current question_number from the question_list
# use input() function to show user the question text and ask for the user's answer
# TODO 5. checking if we're the end of the quiz
# create a still_has_questions() method
# return a boolean depending on the value of question_number
# use while loop to show the next question until the end
# TODO 6. checking if the answer was correct
# create a check_answer() method
# use if-else statement to check if user's answer match the correct answer
# print message depending on right or wrong of user's answer
# TODO 7. keep track user's score
# create a new attribute called score
# the value of score increment by 1 if user's answer is correct
# print user's current score after every question


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
