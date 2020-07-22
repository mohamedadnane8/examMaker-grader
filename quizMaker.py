import random
# this program will generate unordered quizes.

def createQuizes(pathAns,pathQuestion,capitals,n_student):
    for quizNum in range(n_student):
        # TODO: Create the quiz and answer key files.
        quizFile = open(pathQuestion+str(quizNum)+'.txt','w')
        ansFile = open(pathAns+str(quizNum)+'.txt','w')
        quizFile.write('\tID:\n\n\tDate:\n\n')
        ansFile.write('\t\t\t\tAnswers to quiz %s\n' %(quizNum))
        states = list(capitals.keys())
        random.shuffle(states)

        for questionNum in range(len(states)):
            #getting the correct answer
            correct_ans = capitals[states[questionNum]]

            #Getting 3 wrong answers
            wrong_ans = list(capitals.values())
            if correct_ans in wrong_ans:
                wrong_ans.remove(correct_ans)
            wrong_ans = random.sample(wrong_ans,3)

            #Merging these two lists and shuffling them
            answer_options = wrong_ans + [correct_ans]
            random.shuffle(answer_options)

            #Writing the quiz
            quizFile.write('\n\t'+ str(questionNum+1)+'. What is the capital of:'+ states[questionNum] +'\n')
            for i,option in enumerate(answer_options):
                quizFile.write('\t\t'+ 'ABCD'[i] +'. '+option +'\n')
            quizFile.write('\t\t\t'+ 'Ans: ')

            #Writing the answers
            ansFile.write('\t'+ str(questionNum+1)+'. What is thecapital of:' + states[questionNum] +'\n')
            ansFile.write('\t\tAns: '+'ABCD'[answer_options.index(correct_ans)]+' - '+correct_ans +'\n')


# Idea: I want to grade them and write in another file the grade of each student
