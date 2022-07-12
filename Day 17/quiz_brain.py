class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.score=0
        self.question_list=question_list

    def still_has_question(self):
        if len(self.question_number) < len(self.question_number):
            return True 
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower()==current_answer.lower():
            print("You are right")
            self.score+=1
        else:
            print("You are wrong")
        print(f"The correct answer was {current_answer}")
        print(f"Current score is: {self.score}/{self.question_number}")
        print("\n")


     
