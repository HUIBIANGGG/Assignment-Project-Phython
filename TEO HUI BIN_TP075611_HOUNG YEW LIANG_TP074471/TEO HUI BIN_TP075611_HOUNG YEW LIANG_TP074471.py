import Inventory
import Supplier

#TEO HUI BIN, HOUNG YEW LIANG
#TP075611,TP074471
#Program Author

###with open('Distribution.txt','w') as clear:
    #clear.write("")

###with open('ppe.txt','w') as clear:
    #clear.write("")

###with open('Transaction.txt','w') as clear:
    #clear.write("")

#login
def Log_in():
    print("Welcome!!!!")
    userID = input("Enter userID:")
    username = input("Enter username:")
    password = input("Enter password:")
    usertype_choose = input("insert 1 as Admin 2 as user:").strip()

    if usertype_choose == "1":
        usertype_choose = "Admin"
    elif usertype_choose == "2":
        usertype_choose = "User"
    else:
        print("follow the in")
        Log_in()

    usertype = usertype_choose
    all_user_info = [userID, username, password, usertype]


    with open('Users_info.txt', 'r') as File_users:  # read file to check registered user information
        File = File_users.readlines()
        for info in File:
            var = info.strip().split(",")#var=every elements is splited by ","
            if var == all_user_info:
                print("you have logged in")
                if usertype == "Admin":
                    print("welcome" + "," + username)
                    print("")

                    admin_user()

                    print("*" * 20)
                    print("Serve the People,Build our Country")
                    break
                elif usertype == "User":
                    print("welcome" + "," + username)
                    print("")

                    staff()

                    print("*" * 20)
                    print("Serve the People,Build our Country")
                    break
        else:
            print("not logged properly")
            Log_in()



#################################################################################################################


def staff():#for staff
    Inventory.inventory()



#################################################################################################################
# admin funtion
def admin_user():

    def admin_delete(userID):
    # delete user info
        with open("Users_info.txt", "r") as file_delete:
            info = file_delete.readlines()

        with open("Users_info.txt", "w") as file_delete:
            for information in info:
                var = information.strip().split(",")
                if var[0] != userID:
                    file_delete.write(information)

            print("Done")
#################################################################################################################
    def admin_search(usersearch):
        with open("Users_info.txt", "r") as file_search:
            info = file_search.readlines()
            for information in info:
                var = information.strip().split(",")
                if var[0]==usersearch or var[1]==usersearch:
                    print(information)
#################################################################################################################

    def admin_adduser():
        userID = input("Enter userID:")
        username = input("Enter username:")
        password = input("Enter password:")
        confirm_password = input("Enter to confirm password:")
        usertype_choose = input("insert 1 as Admin 2 as user:").strip()
        if usertype_choose == "1":
            usertype_choose = "Admin"
        elif usertype_choose == "2":
            usertype_choose = "User"
        else:
            print("follow the instruction")
        usertype=usertype_choose

        with open('Users_info.txt', 'r') as File_users:  # read file to check overlay user information
            File = File_users.readlines()
            for info in File:
                var = info.strip().split(",")
                if var[0]==userID or var[2]==password or (password!=confirm_password):
                    print("it is overlay or your confirm password is not same")

                    choice=input("if you wanted to continue add user press 1 else any key to exit:")
                    if choice == "1":#continue prompt until no error
                        userID = input("Enter userID:")
                        username = input("Enter username:")
                        password = input("Enter password:")
                        confirm_password = input("Enter to confirm password:")
                        usertype_choose = input("insert 1 as Admin 2 as user:").strip()
                        if usertype_choose == "1":
                            usertype_choose = "Admin"
                        elif usertype_choose == "2":
                            usertype_choose = "User"
                        else:
                            print("follow the instruction")
                        usertype = usertype_choose
                        continue

                    else:
                        return

            else:
                confirmation = input("input c to confirm your information,press B to back to menu:")
                if confirmation == "c" or confirmation == "C":
                    with open('Users_info.txt', "a") as File_users:
                        File_users.write(userID + "," + username + "," + password + "," + usertype + "\n")
                        return

                elif confirmation == "B":
                    return

    def admin_inventory():
        Inventory.inventory()
        return

#################################################################################################################
    while True:

        print("*" * 20)
        user_info=int(input("1 to search user/ 2 to delete user/3 to add new user/ 4 to access inventory/5 to register hospital/6 to read all supplier/7 delete supplier:"))

        if user_info==1:#search specific user
            usersearch=input("corresponding userID or usertype to search")

            admin_search(usersearch)

            Back_to_menu = input("If wanted to continue press C /If wanted to exit press E").strip()
            if Back_to_menu == "C":
                continue#back to menu
            if Back_to_menu == "E":
                break#terminate program

        elif user_info==2:#delte specific user
            userID = input("insert userID to delete corresponding user")
            admin_delete(userID)
            print("*" * 20)
            Back_to_menu = input("If wanted to continue press C /If wanted to exit press E").strip()
            if Back_to_menu == "C":
                continue#back to menu
            if Back_to_menu == "E":
                break#terminate program

        elif user_info==3:#add new user

            admin_adduser()


            print("*" * 20)
            Back_to_menu = input("If wanted to continue Menu press C /If wanted to exit program press E").strip()
            if Back_to_menu == "C":
                continue#back to  menu
            elif Back_to_menu == "E":
                break#terminate program

        elif user_info==4:#acces to inventory

            admin_inventory()

            print("*" * 20)
            Back_to_menu = input("If wanted to continue Menu press C /If wanted to exit program press E").strip()
            if Back_to_menu == "C":
                continue#back to  menu
            elif Back_to_menu == "E":
                break#terminate program


        elif user_info==5:#registration of hospital

            Inventory.Hospital_Hospital()

            print("*" * 20)
            Back_to_menu = input("If wanted to continue Menu press C /If wanted to exit program press E").strip()
            if Back_to_menu == "C":
                continue#back to  menu
            elif Back_to_menu == "E":
                break#terminate program

        elif user_info==6: # read supplier detail

            Supplier.supplier_detail_read()

            print("*" * 20)
            Back_to_menu = input("If wanted to continue Menu press C /If wanted to exit program press E").strip()
            if Back_to_menu == "C":
                continue#back to  menu
            elif Back_to_menu == "E":
                break#terminate program

        elif user_info == 7: #delete supplier
            supplier_code=input("input supplier code to delete")
            Supplier.supplier_delete(supplier_code)
            print("Deletion done")
            print("*" * 20)
            Back_to_menu = input("If wanted to continue Menu press C /If wanted to exit program press E").strip()
            if Back_to_menu == "C":
                continue#back to  menu
            elif Back_to_menu == "E":
                break#terminate program


        else:
            print("follow the instruction")
            print("*" * 20)
            Back_to_menu=input("If wanted to continue press C /If wanted to exit press E").strip()
            if Back_to_menu=="C":
                continue#back to  menu
            if Back_to_menu=="E":
                break#terminate program


#################################################################################################################
#Login or sign in
print("Metropolis Hospital PPE Inventory Management system")
Log_in()







