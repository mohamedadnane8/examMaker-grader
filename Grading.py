import re
number_file = 0
num_question = 50
#open both the quiz and the number file
file_quiz = open('Quiz%s'(number_file),'r')
file_ans = open('AnswerKey%s'(number_file),'r')
question_regex = re.compile(r'(\d)')
ans = re.compile(r'Ans:\s*(\w)',re.IGNORECASE)
# TODO: read Name
# TODO: check if question
# TODO: Find answer chosen and ans in the answerKey
# TODO: check if duplicate
answers = file_ans.readlines()
for line in fileQuiz.readlines():
    if question_regex.search():
        if(line.):
            theAns = ans.search(line)
