import random
# this program will generate unordered quizes.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas'
            : 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan'
            : 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri'
            : 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico'
            : 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota':
                'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem',
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
            'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
# Generate 35 quiz files. w
for quizNum in range(4):
    # TODO: Create the quiz and answer key files.
    quizFile = open('Quiz%s.txt' %(quizNum),'w')
    ansFile = open('AnswerKey%s.txt' %(quizNum),'w')
    quizFile.write('\tName:\n\n\tDate:\n\n\tGrade:\n\n')
    ansFile.write('\t\t\t\tAnswers to quiz %s\n' %(quizNum))
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(50):
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