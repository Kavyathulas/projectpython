contact={}
def display_contact():
    print("name\t\t\t\t CONTACT NUMBER")
    for key in contact:
        print("{}\t\t\t\t{}".format(key,contact.get(key)))

while True:        

    choice=int(input("1. ADD NEW CONTACT /n 2.SEARCH CONTACT\n 3.DISPLAY CONTACT\n4.edit contact\n 5.delete contact\n 6.enter your choice"))
    if choice==1:
        name=input("entername")
        phone=input("enter phone number")
        contact[name]=phone 

    elif choice==2:
        search_name=input("enter your search name")
        if search_name in contact:
            print(search_name,"yes contact number is :",contact[search_name])
        else:
            print('the search name is found in your contact')
    elif choice==3:
            if not contact:
                print("the contact book is empty") 
            else:
                display_contact() 
    elif choice==4:
        edit_contact=input('enter your edit name')
        if edit_contact in contact:
            phone=input("enter your number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("your edit contact number ids not there")  

    elif choice==5:
        del_contact=input("enter the contact to be deleted")
        if del_contact in contact:
            confirm=input("do you want to delete this contact y/n??")
            if confirm=="y" or confirm=="Y":
                contact.pop(del_contact)
            display_contact() 
        else:
                print("name is not found")
    else: 
        break               

                


