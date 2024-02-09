class Quizbrain:
    def __init__(self,qlist):
        self.questionn=0
        self.questlist=qlist
        self.score=0

    def nextq(self):
        current_question=self.questlist[self.questionn]
        self.questionn+=1
        answer=input(f"Q.{self.questionn}:{current_question.text}(True / False)")
        self.checkan(answer,current_question.answer)

    def checkq(self):
        if self.questionn<len(self.questlist):
            return True
        else:
            return False

    def checkan(self,answer,correct):
        if answer.lower()==correct.lower():
            print("You got it right")
            self.score+=1
        else:
            print("You got it whrong")
        print(f"The corrent answer was : {correct} ")
        print(f"Current score {self.score}/{self.questionn}\n")


