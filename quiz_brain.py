class QuizBrain:
    def __init__(self, question_bank):
        self.quest_num = 0
        self.quest_list = question_bank
        self.score = 0

    def still_has_ques(self):
        return self.quest_num < len(self.quest_list)

    def next_question(self):
        text = self.quest_list[self.quest_num].text
        ans = self.quest_list[self.quest_num].answer
        self.quest_num += 1
        user_ans = input(f"Q{self.quest_num} {text} (True/False)? ")
        self.check_answer(user_ans, ans)

    def check_answer(self, user_ans, ans):
        if user_ans.lower() == ans.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("You got it wrong!")
        print("The correct answer was ", ans)
        print(f"Your current score is {self.score} / {(self.quest_num)}")

