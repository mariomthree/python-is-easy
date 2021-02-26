from datetime import date
from os import path
import pickle
import awoc

class FileManipulation:

    def __init__(self, pathFile):
        self.pathFile = pathFile
        self.error = ''

    def all(self):
        if path.exists(self.pathFile):
            with open(self.pathFile, 'rb') as filePickle:
             return pickle.load(filePickle)
        self.error = 'Error: File or directory not found.'
        return []

    def save(self, object):
        contents = self.all() 
        with open(self.pathFile, 'wb') as filePickle:
            contents.append(object)
            pickle.dump(contents, filePickle)
    
    def getError(self):
        return self.error


fileStudent = FileManipulation('students.pickle')
fileQuiz = FileManipulation('quizs.pickle')

class Student:

    def __init__(self, studentId, names, gender, yearOfBoth, phoneNumber, countryCode, countryName, course, work):
        self.studentId = studentId
        self.names = names
        self.gender = gender
        self.yearOfBoth = yearOfBoth
        self.phoneNumber = phoneNumber
        self.countryCode = countryCode
        self.countryName = countryName
        self.course = course
        self.work = work

    def getYearsOld(self):
        return date.today().year - self.yearOfBoth

    def getAllDataOfStudent(self):
        print(f"Names: {self.names}")
        print(f"Gender: {self.names}")
        print(f"Year of both: {self.yearOfBoth}")
        print(f"Phone Number: {self.phoneNumber}")
        print(f"Code Country: {self.countryCode}")
        print(f"Country Name: {self.countryName}")
        print(f"Curse: {self.course}")
        print(f"Work: {self.work}")


    def getQuizs(self):
        quizs = fileQuiz.all() 
        for quiz in quizs:
            if quiz.studentId == self.studentId:
                return quiz
        return -1

    
    def removeSignalPlusIncountryCodeAndReturnFirstNumber(self, countryCode):
        return countryCode[:3] if countryCode[0] == '+' else countryCode[:2]

    
    def verifyQualificationFemale(self):
        countryCode = int(self.removeSignalPlusIncountryCodeAndReturnFirstNumber(self.countryCode))
        if self.getYearsOld() > 20 and \
                countryCode == 25 and \
                75 <= self.getQuizs().calculateAndReturnAverageOfQuiz() <= 80 and \
                self.countryName in awoc.AWOC().get_countries_list_of("africa"):
            return True
        return False


    def verifyQualificationMale(self):
        return True if self.getQuizs().calculateAndReturnAverageOfQuiz() >= 80 else False


    def verifyQualification(self):
        quizAverage = self.getQuizs().calculateAndReturnAverageOfQuiz()
        if self.gender.upper() == 'M':
            return self.verifyQualificationMale()
        return self.verifyQualificationFemale()

class Quiz:

    def __init__(self, studentId, scoreOfFirstQuiz, scoreOfSecondQuiz, scoreOfThirdQuiz, scoreOfFourQuiz):
        self.studentId = studentId
        self.scoreOfFirstQuiz = scoreOfFirstQuiz
        self.scoreOfSecondQuiz = scoreOfSecondQuiz
        self.scoreOfThirdQuiz = scoreOfThirdQuiz
        self.scoreOfFourQuiz = scoreOfFourQuiz

    def calculateAndReturnAverageOfQuiz(self):
        return (self.scoreOfFirstQuiz + self.scoreOfSecondQuiz + self.scoreOfThirdQuiz + self.scoreOfFourQuiz) / 4


        
def main():
    while True:
        print('\nChoose an option')
        print('1. Add Student')
        print('2. View Students')
        print('3. Search Student')
        print('4. Exit')
        option = int(input('>> '))

        if option == 1:
            
            studentId = len(fileStudent.all()) + 1
            names = input("Enter student's full names: ")
            gender = input("Enter student's gender[M/F]: ")
            yearOfBirth = int(input('Enter the year of birth: '))
            course = input("Enter the course name: ")
            phoneNumber = int(input("Enter the phone number: "))
            countryCode = input("Enter the code country: ")
            countryName = input("Enter the country name: ")
            print('Select your occupation:')
            print('1 -> College student')
            print('2 -> Working adult')
            work = input(">> ")

            scoreOfFirstQuiz = float(input("Enter score for first Quiz: "))
            scoreOfSecondQuiz = float(input("Enter score for second Quiz: "))
            scoreOfThirdQuiz = float(input("Enter score for third Quiz: "))
            scoreOfFourQuiz = float(input("Enter score for four Quiz: "))

            student = Student(studentId, names, gender, yearOfBirth, phoneNumber, countryCode, countryName, course, work)
            quiz = Quiz(studentId, scoreOfFirstQuiz, scoreOfSecondQuiz, scoreOfThirdQuiz, scoreOfThirdQuiz)
            
            fileStudent.save(student)
            fileQuiz.save(quiz)
            
            print("Student registed.")
        
        elif option == 2:
            students = fileStudent.all()
            if len(students) > 0:
                print('\nNames\t\tGender\tCourse\tCountry Code\tAverage Quiz\tQualify Scholarship')
                for student in students:
                    status = "Confirmed" if student.verifyQualification() else "Failed"
                    print(f'{student.names}\t{student.gender}\t{student.course}\t{student.countryCode}\t\t{student.getQuizs().calculateAndReturnAverageOfQuiz()}\t\t{status}')
            else:
                print('\nStudent not found. Please register.')
        elif option == 3:
            name = input("Enter a name of student: ")
            students = fileStudent.all()
            isFinded = False
            for student in students:
                if student.names == name:
                    isFinded = True
                    student.getAllDataOfStudent()
                    break
            if isFinded == False:
                print('Student not found.')

        elif option == 4:
            print("\nBye!")
            break
        else:
            print('\nOption not found. Type again.')

main()