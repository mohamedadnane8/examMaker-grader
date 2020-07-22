from quizMaker import createQuizes
from Grading import grade
def Main():
    number_student = 30
    quiz_semipath = 'Quiz'
    ans_semipath = 'AnsKey'
    #these are the questions with their correct answer as a dictionary
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
    print('Please Imput 1 to create the quiz and 2 to grade it.')
    choice = int(input())
    if choice == 1:
        createQuizes(ans_semipath,quiz_semipath,capitals,number_student)
    elif choice == 2:
        for i in range(number_student):
            grade(ans_semipath,quiz_semipath,i,50)
if __name__ == '__main__':
    Main()
