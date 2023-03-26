from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data.get('results'):
    question_bank.append(Question(data.get('question'), data.get('correct_answer')))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print('You\'ve Completed The Quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')
