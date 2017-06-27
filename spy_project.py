spy_list=['Aarav','22','4.5']
spy_details={'Gauri':{'age':20,'rating':5,'status':'','friend':[],'salutation':[]}}
status_history={'online','offline','busy','Available'}
def spy_friend(user_name):
    f_name=raw_input("Enter the friend name: ")
    if len(f_name)!=0:
        f_age = int(raw_input("Enter your friend age"))
        if f_age > 12 and f_age < 50:
            f_rating = float(raw_input("enter the rating"))
            spy_details[user_name]['friend'].append(f_name)
            print "your friend added in list"
        else:
            print "You cannot be added \n"
    else:
        print "Your name is not accurate"

def spy_status(user_name):
    print spy_details[user_name]['status']
    status_choice=int(raw_input("1.Upadte  status \n2.Add new status"))
    if status_choice==1:
        print spy_details[user_name]['status']
        status1=raw_input("update your status:")
        spy_details[user_name]['status']=status1
        print "Your status updated successfully!"
    elif status_choice==2:
        status2=raw_input("Enter the new status:")
        spy_details[user_name].update({status2:status})
        print "new status added successfully!"
    else:
        print "Innvalid choice!"

choice=True
while choice==True:
    user_name=raw_input("Enter your name:")
    if user_name in spy_details:

        print "Welcome %s %s." % (spy_details[user_name]['salutation'], user_name)
        status_menu = int(raw_input(
            "1.Add a status update \n2.Add a friend \n3.send a secret message \n4.Read a secret message \n5.Read chats rom user \n6. Close application"))
        if status_menu == 1:
            spy_status(user_name)
        elif status_menu == 2:
            spy_friend(user_name)
        elif status_menu == 3:
            spy_encoded()
        elif status_menu == 4:
            spy_messsage()
        elif status_menu == 5:
            spy_history()
        else:
            print "Invalid input"
    else:
        if len(user_name)==0:
            print "Error something wrong happen"
            exit()
        else:
            input_salutation=raw_input("Enter the salutation")
            age=int(raw_input("enter the age of spy"))
            if 12<age<50:
                status = raw_input("Enter the status of user")
                ratings = float(raw_input("enter the ratings"))
                if ratings == 1:
                    print "Not good!"
                elif ratings > 1 and ratings <= 5:
                    print  "Good"
                elif ratings > 5 and ratings <= 10:
                    print "Excellent"
                else:
                    print "Wrong choice!"
                spy_details.update({user_name:dict(salutation=input_salutation,age=age,status=status,ratings=ratings)})
                print "you added successfully in spychat!"
                print "Welcome %s %s %s %i %i" %(spy_details[user_name]['salutation'],user_name,status,age,ratings)
                print spy_details.keys()
            else:
                print "your age is not appropriate!"
                exit()
        ch=raw_input("enter the option 'y' for  yes or other key")
        if ch=='y':
            continue
        else:
            exit()



