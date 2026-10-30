import json
import random
import string
from pathlib import Path # importing the Path class from the pathlib module deals with the file folder path

# there is the main datafile json which stores all the data 
# but we first create a dummy data and transfer all the data from the json to the dummy data 
# we do all the updation , deletion , creation on the dummy file and when all the operation is end we agian transfer the data from the dummy to the json file 
# we done this because the json is not in this file and dummy is in the file 


class Bank:
    database = 'data.json' # saving the path of the json file
    data = [] # dummy data
    try :
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read()) # we read all the data in the json and then put in the dummy 
        else : 
            print("no such file exist")    
    except Exception as err:
        print(f"an exception occured as {err}")
    

    # updating the data from the dummy file to the json file
    @classmethod 
    def __update(cls):
        with open(cls.database,'w') as fs :
            fs.write(json.dumps(Bank.data)) # so basically we are transfering the data in the dummy file(data) to the json file


    # generating the account no 
    @classmethod
    def __accountgenerate(cls) : 
        alpha = random.choices(string.ascii_letters,k=3) # choosing 3 random letters from the all english letters
        num = random.choices(string.digits,k=3) # choosing 3 numbers
        spchar = random.choices("!@#$%^&*",k=1) # choosing 1 special character
        id = alpha + num + spchar
        random.shuffle(id) # so that all the things mixup randomly
        return "".join(id) # we get a string finally by adding id into a empty string

    def Createaccount(self):
        # asking the user for the data
        info = {
            "Name" : input("Tell your Full name :- "),
            "Age" : int(input("Tell me your age :- ")),
            "E_mail" : input("Enter your email Id :- "),
            "Pin" : int(input("Tell your pin :- ")),
            "Account_No" : Bank.__accountgenerate(), # generating a unique account no
            "Balance" : 0
        }
        if info['Age'] < 18 or len(str(info['Pin'])) != 4 :
            print("Sorry you cannot create your account")
        else:
            print(f"{info['Name']} your Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info) # we append the info(user details) into our dummy file(data) which is inside the Bank class


            Bank.__update() # transfering the details(data/info) into the json file 


    def depositemoney(self):
        # asking the user for his particular acc_no and pin
        acc_no = input("Please tell your account number:- ")
        pin = int(input("Please enter your pin:- "))

        # so there in the json file there is many dictionaries one for each user
        # so we execute a loop and only take the dictionary which the user data(account no and pin) matches
        # i here representing the dictionaries in the data(dummy file) 
        # then the particular dictionary stored into the userdata

        userdata = [i for i in Bank.data if i['Account_No'] == acc_no and i['Pin'] == pin] # Account_No , Pin is the keyword of the dictionaries and acc_no and pin is the variables we take in this particular function

        if userdata == False : # if it is a empty string it produces a falsy data (0)
            print("Sorry no data found")

        else : # what are the things we update here they will directly update in data(dummy file)
            amount = int(input("How much money you want to deposite:- "))
            if amount > 10000 and amount < 0 :
                print("Sorry the amount is too much you can deposite only below 10000 and above 0 ")
            else:
                print(userdata)
                userdata[0]['Balance'] += amount     # so the amount is deposited means in the particular dictionary Balance(key) value is modified
                # here userdata is a list and that list's first element is the dictionary we are working that's why extra zero representing the first element
                Bank.__update() # updating the changes from the dummy file(data) to the json file
                print(f"{amount} deposited successfully")
                print(f"Your Current Balance : {userdata[0]['Balance']}")


    def withdrawmoney(self):
        # asking the user for his particular acc_no and pin
        acc_no = input("Please tell your account number:- ")
        pin = int(input("Please enter your pin:- "))

        # by the help of this data finding the dictionary 

        userdata = [i for i in Bank.data if i['Account_No'] == acc_no and i['Pin'] == pin] 

        if userdata == False : # if it is a empty string it produces a falsy data (0)
            print("Sorry no data found")

        else : # what are the things we update here they will directly update in data(dummy file)
            amount = int(input("How much money you want to withdraw:- "))
            if amount>userdata[0]['Balance'] :
                print("Sorry you don't have that much money ")
    
            else:
                print(userdata)
                userdata[0]['Balance'] -= amount     # so the amount is withdrawn means in the particular dictionary Balance(key) value is modified
                # here userdata is a list and that list's first element is the dictionary we are working that's why extra zero representing the first element
                Bank.__update() # updating the changes from the dummy file(data) to the json file
                print(f"{amount} Withdrew successfully")
                print(f"Your Current Balance : {userdata[0]['Balance']}")
    


    def showdetails(self):
        # asking the user for his particular acc_no and pin
        acc_no = input("Please tell your account number:- ")
        pin = int(input("Please enter your pin:- "))

        # by the help of this data finding the dictionary 

        userdata = [i for i in Bank.data if i['Account_No'] == acc_no and i['Pin'] == pin] 

        if userdata == False : # if it is a empty string it produces a falsy data (0)
            print("Sorry no data found")
        else :
            print("Your information are \n\n\n")
            # we are traversing in the first element(dictionary) of the list
            for i in userdata[0]: # i here representing the keys of the dictionary
                print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
         # asking the user for his particular acc_no and pin
        acc_no = input("Please tell your account number:- ")
        pin = int(input("Please enter your pin:- "))

        # by the help of this data finding the dictionary 

        userdata = [i for i in Bank.data if i['Account_No'] == acc_no and i['Pin'] == pin] 

        if userdata == False:
            print("no such data found")
        else:
            print("You can not change the age, account number, balance ")

            print("Fill the details for change or leave it empty if no change:- ")
            # we are creating a new dummy data , we update in that and then transfer to the data(dummy data file ) and then to the json file
            newdata = {
                "Name" : input("Please Enter the new name or press enter:- "),
                "E_mail" : input("Please enter the new mail id or press enter to skip :- "),
                "Pin" : input("Enter the new Pin or press enter to skip :- ")
            }

            if newdata["Name"] == "" :
                newdata["Name"] = userdata[0]['Name']
            if newdata["E_mail"] == "" :
                newdata["E_mail"] = userdata[0]['E_mail']
            if newdata["Pin"] == "" :
                newdata["Pin"] = userdata[0]['Pin']
            
            newdata["Age"] = userdata[0]['Age']
            newdata["Account_No"] = userdata[0]['Account_No']
            newdata["Balance"] = userdata[0]['Balance']

            # checking the pin is string or integer
            if type(newdata['Pin']) == str :
                newdata['Pin'] = int(newdata['Pin'])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
            Bank.__update()
            print("Details updated successfully")


    def deleteaccount(self):
        # asking the user for his particular acc_no and pin
        acc_no = input("Please tell your account number:- ")
        pin = int(input("Please enter your pin:- "))

        # by the help of this data finding the dictionary 

        userdata = [i for i in Bank.data if i['Account_No'] == acc_no and i['Pin'] == pin] 

        if userdata == False:
            print("no such data found")
        else:
            check = input("press y if you actually want to delete the account or press n")
            if check == 'n' or check == 'N' :
                print("bypass")
            else:
                index = Bank.data.index(userdata[0]) # finding the index in the dummy file list(data) of the particular userdata[0] dictionary
                # .index(ele) returns the index(position) of the element in the list
                Bank.data.pop(index) # Bank.data is the list and we are deleting the particular element(dictionary)
                print("Account is deleted successfully")
                Bank.__update()



user = Bank()

print("press 1 for creating a account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money form the bank ")
print("press 4 for details ")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response:- "))

if check == 1 :
    user.Createaccount()

if check == 2 :
    user.depositemoney()

if check == 3 :
    user.withdrawmoney()

if check == 4 :
    user.showdetails()

if check == 5 :
    user.updatedetails()

if check == 6 :
    user.deleteaccount()

