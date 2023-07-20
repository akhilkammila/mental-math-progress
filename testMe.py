import random
import time
from enum import Enum
from typing import List, Tuple
import operator

class Operation(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4

    def __str__(self):
        if self.value == 1: return "+"
        if self.value == 2: return "-"
        if self.value == 3: return "*"
        if self.value == 4: return "/"
    
    def returnOperator(self):
        if self.value == 1: return operator.add
        if self.value == 2: return operator.sub
        if self.value == 3: return operator.mul
        if self.value == 4: return operator.truediv

class QuestionInstance:
    def __init__(self, leftOperand: int, rightOperand: int, operation: Operation):
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand
        self.operation = operation

    def __str__(self):
        return str(self.leftOperand) + ' ' + str(self.operation) + ' ' + str(self.rightOperand)

class Question:
    def __init__(self, rangeBegin: int, rangeEnd: int, operation: Operation):
        self.rangeBegin = rangeBegin
        self.rangeEnd = rangeEnd
        self.operation = operation
    
    def generate_instance(self):
        val1 = random.randrange(self.rangeBegin, self.rangeEnd + 1)
        val2 = random.randrange(self.rangeBegin, self.rangeEnd + 1)
        return QuestionInstance(val1, val2, self.operation)

class QuestionSet:
    def __init__(self, questions: List[Question]):
        self.questions = questions
    
    def generate_instance(self):
        questionType: Question = random.choice(self.questions)
        return questionType.generate_instance()

class Game:
    def __init__(self, gameLength: int, questionSet: QuestionSet):
        self.gameLength = gameLength
        self.questionSet = questionSet

        self.askedQuestions = []
        self.answers = []
    
    def run_game(self):
        start_time = time.time()
    
            
if __name__ == "__main__":
    mixed: QuestionSet = QuestionSet([Question(11, 99, Operation.ADD), Question(11, 99, Operation.SUBTRACT)])
