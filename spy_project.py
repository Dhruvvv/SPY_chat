spy_detail={}
spy_status_history={}
status=["Available","sleeping"],"Busy","online"]
special_words=["sos","save_me","help_me"]
count=0

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
    status_choice=int(raw_input("1.Update  status \n2.Add new status"))
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
        print "Invalid choice!"

def select_a_friend(user_name):
    leng=len(spy_detail[user_name]["friends"])
    if leng==0:
        print "You have no friends added. \n"
        return("null")
    else:
        print "You have following people in your friend list: \n"
        for i in range(0,leng):
            print str(i+1)+". "+str(spy_detail[user_name]["friends"].keys()[i])
        position=int(raw_input("Enter the number corresponding to your choice of friend with whom you want to continue: "))
        position=position-1
        if (position<0 or position>=leng):
            print "You have entered a wrong input\nTry again.\n"
            return("null")
        else:
            return(position)


choice=True
while choice==True:
    user_choice=int(raw_input("Do you want to continue using \n1.Default user \n2.Create a new spy_useruser"))
    if user_choice==1:
        import spy_details
        user_name=spy_details.default_spy_details.keys()[0]
        if user_name in spy_details.keys():
            print "Default user exist in spy_dictionary"
        else:
            spy_details.update(spy_details.default_spy_detail)
            spy_status_history.update({user_name: []})
    elif user_choice==2:
        user_name=raw_input("Enter the user")
        if len(user_name)<1:
            print "Name is invalid Try something else"
            #print "Welcome %s %s." % (spy_details[user_name]['salutation'], user_name)
        else:
            input_salutation=raw_input("Enter the salutation")
            age=int(raw_input("enter the age of spy"))
            if 12>=age<=50:
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
    status_menu = int(raw_input("1.Add a status update \n2.Add a friend \n3.send a secret message \n4.Read a secret message \n5.Read chats rom user \n6. Close application"))
    if status_menu == 1:
        spy_status(user_name)
    elif status_menu == 2:
        friennds_count=spy_friend(user_name)
        print  "Your %i friends as" %(friends_count)
    elif status_menu == 3:
        select_a_friend()
    elif status_menu == 4:
        read_messsage(user_name)
    elif status_menu == 5:
        chat_read(user_name)
    elif status_menu==6:
          exit()
    else:
        print "Invalid input"



