def getContacts():
    return (
        ('Liam',820011234,'liam@gmail.com'),
        ('Noah',840011001,'noam@ovi.com'),
        ('Tony',861230023,'tony@hotmail.com'),
        ('Bert',830011021,'bert@hi.com')
    )

def searchContacs(name):
    contacts = getContacts()
    for contact in contacts:
        if str(contact[0]).lower() == name.lower():
            return contact
            break
    return -1

def showDetailsContact(contact):
    if contact == -1:
        print("Contact not found.")
    else:
        print(contact) 

name = input('Enter a name for search: ')
contact = searchContacs(name)
showDetailsContact(contact)
