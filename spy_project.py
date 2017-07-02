from steganography.steganography import Steganography
spy_list={}
status_history={}
status=["Available","sleeping","Busy","online"]
count=0
def spy_friend(user_name):
    f_name=raw_input("Enter the friend name:")
    if len(f_name)!=0:
        f_age = int(raw_input("Enter your friend age"))
        if f_age > 12 and f_age < 50:
            f_rating = float(raw_input("enter the rating"))
            if f_rating < spy_list[user_name]['rating']
                print "this can not be added in your friendlist. "
            else:
                spy_list[user_name]['friends'].update({f_name:{'f_age':f_age,'f_rating':f_rating,"chat":{}}})
                print "your friend added in your list"
        else:
            print "You cannot be added.\n"
            return ()
    else:
            print "Invalid name!"
            return ()
        print len(spy_list[user_name]['friends'])

def spy_status(user_name):
    print spy_details[user_name]['status']
    status_choice=int(raw_input("1.Update Status \n2.Add new status\n3.Choose from pre-defined status"))
    if status_choice==1:
        print "Your current status is: "+spy_details[user_name]['status']
        for i in range(len(status_history[user_name])):
            print str(i+1)+". " + str(status_history[user_name][i])
        select=int(raw_input("Choose option from above: "))
        select=select - 1
        if select + 1 > len(status_history[user_name]):
            print "Wrong input! Plz enter right option."
            return
        else:
            spy_list[user_name]['status'] = status_history[user_name][select]
            print "Your status updated successfully!"
    elif status_option == 2:
        status2 = raw_input("Enter your new status:")
        spy_list[user_name].update({'status': status2})
        print "Your new status added successfully!"
        if status2 not in status_history[user_name]:
            status_history[user_name].append(status2)
    elif status_option == 3:
        for i in range(len(status)):
            print str(i + 1)+". " + str(status[i])
        select= int(raw_input("Enter the choice: "))
        select= select - 1
        if select + 1 > len(status_history[user_name]):
            print "Wrong input! Plz enter right option."
            return
        else:
            spy_list[user_name]['status'] = status[select]
            if status[select] not in status_history[user_name]:
                status_history[user_name].append(status[select])
            print "Your status updated successfully!"
    else:
        print "Invalid option!"
    print spy_list[user_name]['status']

def select_a_friend(user_name):
    friend_list = len(spy_list[user_name]['friends'].keys())
    if friend_list==0:
        print "You have no friends added. \n"
        return("null")
    else:
        print "You have following people in your friend list: \n"
        for i in range(0,leng):
            print str(i+1)+". "+str(spy_details[user_name]["friends"].keys()[i])
        position=int(raw_input("Enter the number corresponding to your choice of friend with whom you want to continue: "))
        position=position-1
        if (position<0 or position>=friend_list):
            print "You have entered a wrong input\nTry again.\n"
            return("null")
        else:
            return(position)
def send_a_message(user_name):
    global flag
    position = select_a_friend(name)
    if position == 'null':
        return (0)
    else:
        f_name = spy_list[user_name]['friends'].keys()[position]
        from steganography.steganography import Steganography
        path_name = "C:\Users\Sony\Desktop"
        img_name = raw_input("What is the name of your image?: ")
        path = path_name +"\\" + img_name
        print "your path with specified image name is: " + path
        d_img_name = raw_input("What name should be the output file?: ")
        d_path = "C:\Users\Sony\Desktop"
        overall_path = d_path + "\\" + d_img_name
        print overall_path
        text = raw_input("Enter the TEXT to encode: ")
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        flag = flag + 1
        spy_list[user_name]['friends'][f_name]['chat'].update({flag: {"secret_message": text, "time": date,"boolean": True}})
        print "keep calm..................................."
        q= text.strip().split(" ")
        Steganography.encode(path, overall_path, text)
        print "\nMessage has been encoded and sent to %s.\n" % (
            str(spy_list[user_name]['friends'].keys()[position]))
def read_a_message(user_name):
    global flag
    position = select_a_friend(name)
    if position == "null":
        return ()
    else:
        from steganography.steganography import Steganography
        f_name = spy_list[user_name]['friends'].keys()[position]
        print "Friend %s selected\n" % (f_name)
        d_img_name = raw_input("What is the name of the output file you want to decode?: ")
        d_path = "C:\Users\Sony\Desktop"
        overall_path = d_path+"\\"+ d_img_name
        from datetime import datetime
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print "come down...................................."
        secret_text = Steganography.decode(overall_path)
        if len(secret_text) == 0:
            print "Image has no secret message"
        else:
            print "\nYour secret text is: " + secret_text
def chat_read(user_name):
    position = select_a_friend(user_name)
    if position == "null":
        return ()
    f_name = spy_list[user_name]["friends"].keys()[position]
    print "Chat history:\n"
    print spy_list[user_name]["friends"][f_name]["chat"]

def menu(spy_c):
    status_menu = int(raw_input("1.Add a status update \n2.Add a friend \n3.send a secret message \n4.Read a secret message \n5.Read chats rom user \n6. Close application"))
    if status_menu == 1:
        spy_status(user_name)
    elif status_menu == 2:
        friends_count=spy_friend(user_name)
        print  "Your %i friends as" %(friends_count)
    elif status_menu == 3:
        select_a_friend()
    elif status_menu == 4:
        read_message(user_name)
    elif status_menu == 5:
        chat_read(user_name)
    elif status_menu==6:
          exit()
    else:
        print "Invalid input"
        continue
exit()

choice=True
while choice==True:
    user_choice=int(raw_input("Do you want to continue using \n1.Default user \n2.Create a new spy_user"))
    if user_choice==1\:
        user_name=raw_input("Enter your name: ")
        if user_name in spy_details:
            menu(user_name)
        else:
            print "You are not a SPY"
    elif user_choice==2:
        user_name=raw_input("Enter the user")
        if len(user_name)<1:
            print "Name is invalid Try something else"
        else:
            input_salutation=raw_input("Enter the salutation")
            age=int(raw_input("enter the age of spy"))
            if 12>=age<=50:
                ratings = float(raw_input("enter the ratings"))
                if ratings>-1:
                    print "sir please enter ratings in positive"
                elif ratings < 11:
                    print "Rating cannot be greater"
                else:
                    print "Wrong choice!"
                spy_details.update({user_name:dict(salutation='input_salutation',age='age',status='status',ratings='ratings')})
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