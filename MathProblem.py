import random

OPERATORS = ["+", "-","*", "/"]
MIN_OPERAND = 3
MAX_OPERAND = 12

class MathProblem:
    playCtr = 0

    def __init__(self):
        self.left = random.randint(MIN_OPERAND, MAX_OPERAND)
        self.right = random.randint(MIN_OPERAND, MAX_OPERAND)
        self.operator = random.choice(OPERATORS)

    def generateProblem(self):

        while (self.right == 0 and self.left == 0):
            self.right = self.setNewRight(self.right)
            self.left = self.setNewLeft(self.left)

        if(self.operator == "/" and self.right > self.left):
            temp = self.right
            self.right = self.left
            self.left = temp



        problem = str(self.left) + " " + self.operator + " " + str(self.right)
        return problem

    def generateAnswer(self, problem):
        answer = 0
        match self.operator:
            case "+":
                answer = self.left + self.right
                answer = round(answer, 2)
            case "-":
                answer = self.left - self.right
                answer = round(answer, 2)
            case "*":
                answer = self.left * self.right
                answer = round(answer, 2)
            case "/":
                answer = self.left / self.right
                answer = round(answer, 2)
                if(answer % 2 == 0):
                    answer = int(self.left / self.right)
        return answer


    def setNewLeft(self,left):
        self.left = random.randint(MIN_OPERAND, MAX_OPERAND)

    def setNewRight(self,right):
        self.right = random.randint(MIN_OPERAND, MAX_OPERAND)

    def setNewOperator(self,operator):
        self.operator = random.choice(OPERATORS)

    @classmethod
    def main(cls):
        if(cls.playCtr < 1):
            print("Welcome to the math game, I hope you survive. ")
            cls.playCtr += 1
        while True:
            problem_instance = cls()
            problem = problem_instance.generateProblem()
            answer = problem_instance.generateAnswer(problem)
            print(problem)
            userInput = input("Please enter your answer to the problem above (Round to 2 decimal places)")
            if userInput.lower() == "q":
                print("Quitting the game. Thanks for playing!")
                break
            while(userInput != str(answer)):
                print("Wrong!")
                userInput = input("Please try again")
            print("Correct!")

if __name__ == "__main__":
    MathProblem.main()




