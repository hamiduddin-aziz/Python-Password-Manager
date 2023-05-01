
# Project: Password manager 

def view():
    with open("pwd_list.txt", "r") as list:
        for line in list.readlines():
            data = line.rstrip()
            user,pswd = data.split("|")
            print("User: ", user,"| Password: ",pswd)


def add():
    name = input("Account Name ")
    pwd = input("Password ")
    with open("pwd_list.txt", "a") as list:
        list.write(name + "|" + pwd + "\n")

MasPwd = "a"
count = 0

while count < 3:
    Master_pwd = input("Welcome. What is the master password? ")
    if Master_pwd != MasPwd:
        count += 1
        print("Wrong password. You have", 3 - count, "tries left.")
    else:
        print("Welcome")
        break

if count == 3:
    print("You have reached your limit of 3 tries. Goodbye.")
    quit()
    
while True:
    mode = input("What would you like to do with password manager? add , view or quit? ").lower()
    if mode == "quit":
        print("Goodbye")
        quit()

    elif mode == "add":
        add()

    elif mode == "view":
        view()

    else:
        print("Command not recognizable")
