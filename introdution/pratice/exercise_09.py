
phoneBook = {
}
person = {
    'firstName': '',
    'lastName': '',
    'phoneNumber':'',
    'email':'',
    'homeAddress':'',
    'city':'',
    'state':'',
    'zipCode':''
}

def addPerson(person):
    lengthOfPhoneBook = len(phoneBook)
    if lengthOfPhoneBook == 0:
        phoneBook[1] = person
    else:
        phoneBook[lengthOfPhoneBook+1] = person

def getPhoneBook():
    return phoneBook

def getPersonOfIndex(index):
    return phoneBook[index]

while True:
    print("\n1. Add person")
    print("2. View phone book")
    print("0. Exit")
    option  = input(">> ")

    if option == '1':
        person['firstName'] = input('First name: ')
        person['lastName'] = input('Last name: ')
        person['phoneNumber'] = input('Phone number: ')
        person['email'] = input('E-mail: ')
        person['homeAddress'] = input('Home address: ')
        person['city'] = input('City: ')
        person['state'] = input('State: ')
        person['zipCode'] = input('Zip Code: ')
        addPerson(person)
    elif option == '2':
        print(getPhoneBook())
    elif option == '0':
        break
    else:
        print("Not found option.")
