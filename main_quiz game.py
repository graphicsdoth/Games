from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
l= len(question_data)
##creating a list of all questions
for i in question_data:
    q_obj = Question(i["question"], i["correct_answer"])
    question_bank.append(q_obj)

 ## creating an object for class QuizBrain
ques = QuizBrain(question_bank)

ques.next_question()
while(ques.still_has_ques() == True):
    ques.next_question()

print("\n")
print("You have completed the quiz")
print(f"Your Final Score is {ques.score}/{ques.quest_num}")



