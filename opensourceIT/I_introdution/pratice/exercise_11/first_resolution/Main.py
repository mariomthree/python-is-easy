from datetime import date
import awoc

def calculateAndReturnAverageOfQuiz(listOfScore):
    numberOfQuiz = len(listOfScore)
    sumOfScore = 0
    for score in listOfScore:
        sumOfScore += score
    return sumOfScore / numberOfQuiz


def removeSignalPlusIncountryCodeAndReturnFirstNumber(countryCode):
    return countryCode[:3] if countryCode[0] == '+' else countryCode[:2]


def verifyQualificationFemale(yearOfBirth, countryName, countryCode, quizAverage):
    studentAge = date.today().year - yearOfBirth
    countryCode = int(removeSignalPlusIncountryCodeAndReturnFirstNumber(countryCode))
    if studentAge > 20 and \
            countryCode == 25 and \
            75 <= quizAverage <= 80 and \
            countryName in awoc.AWOC().get_countries_list_of("africa"):
        return True
    return False


def verifyQualificationMale(quizAverage):
    return True if quizAverage >= 80 else False


def verifyQualification(gender, yearOfBirth, countryName, countryCode, quizAverage):
    if gender.upper() == 'M':
        return verifyQualificationMale(quizAverage)
    return verifyQualificationFemale(yearOfBirth, countryName, countryCode, quizAverage)


def checkGradeAndReturnResult(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 75:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"


def showMessageOfStudentStatus(grade, qualificationStatus):
    print(f"\nYou grade is {grade}. Wich is an {checkGradeAndReturnResult(grade)}.")
    if 75 <= grade <= 90 and qualificationStatus:
        print(f"Congratulation! you Qualify for a Scholarship.")
    elif grade >= 60:
        print(f"Sorry you have failed the class.")
    else:
        print(f"You may wanna consider retaking this class.")


names = input("Enter student's full names: ")
gender = input("Enter student's gender[M/F]: ")
course = input("Enter the course name: ")
phoneNumber = int(input("Enter the phone number: "))
countryCode = input("Enter the code country: ")
countryName = input("Enter the country name: ")
print('Select your occupation:')
print('1 -> College student')
print('2 -> Working adult')
work = input(">> ")
yearOfBirth = int(input('Enter the year of birth: '))
scoreOfFirstQuiz = float(input("Enter score for first Quiz: "))
scoreOfSecondQuiz = float(input("Enter score for second Quiz: "))
scoreOfThirdQuiz = float(input("Enter score for third Quiz: "))
scoreOfFourQuiz = float(input("Enter score for four Quiz: "))

grade = quizAverage = calculateAndReturnAverageOfQuiz([scoreOfFirstQuiz,
                                                       scoreOfSecondQuiz,
                                                       scoreOfThirdQuiz,
                                                       scoreOfFourQuiz
                                                       ])

qualificationStatus = verifyQualification(gender,
                                          yearOfBirth,
                                          countryName,
                                          countryCode,
                                          quizAverage
                                          )
showMessageOfStudentStatus(grade, qualificationStatus)

with open('data.txt', 'w') as fileText:
    content = f'Names: {names}' \
              f'\nGender: {gender}' \
              f'\nCourse: {course}' \
              f'\nPhone number: {phoneNumber}' \
              f'\nCountry code: {countryCode}' \
              f'\nCountry name: {countryName}' \
              f'\nWork: {work}' \
              f'\nYear of Birth: {yearOfBirth}' \
              f'\nResult of Quiz:' \
              f'\nQuiz 1: {scoreOfFirstQuiz}' \
              f'\nQuiz 2: {scoreOfSecondQuiz}' \
              f'\nQuiz 3: {scoreOfThirdQuiz}' \
              f'\nQuiz 4: {scoreOfFourQuiz}'
    fileText.write(content)

with open('data.txt', 'r') as fileText:
    print(fileText.read())
