import re
def grade(pathAns,pathQuestion,number_file,num_question):
    #open both the quiz and the answerkey file
    file_quiz = open(pathQuestion+str(number_file)+'.txt')
    file_ans = open(pathAns+str(number_file)+'.txt')
    question_regex = re.compile(r'(\d)')
    ans_regex = re.compile(r'Ans:\s*(\w)',re.IGNORECASE)
    #  read ID
    ID_regex = re.compile(r'ID:\s*(\d*)',re.IGNORECASE)
    ID = ID_regex.search(file_quiz.readline()).group(1)
    if len(ID) == 0:
        return
    answers = file_ans.readlines()

    grade = 0
    i = 0

    for line in file_quiz.readlines():
        if question_regex.search(line):
            #get the answer from  the ansKey
            for iter in range(i+1,len(answers)):
                if(ans_regex.search(answers[iter])):
                    theAns = ans_regex.search(answers[iter]).group(1)
                    i = iter
                    break
                    #I guess I have to change this to list[0]
        if len(ans_regex.findall(line)) != 0:
            if ans_regex.search(line).group(1) == theAns:
                print('Correct Answer!')
                grade += 100 / num_question
            #check if answer is correct + add grades.
    file_grade = open(ID+ 'txt','a')
    file_grade.write('Quiz: '+ str(number_file) + str(grade))
