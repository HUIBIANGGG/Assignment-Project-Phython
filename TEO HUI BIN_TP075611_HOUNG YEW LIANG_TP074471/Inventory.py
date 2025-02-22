import Supplier
import datetime

#TEO HUI BIN, HOUNG YEW LIANG
#TP075611,TP074471
#Program Author

#with open('Hospitals.txt','w') as Clear:
    #Clear.write("")
#with open('supplier.txt','w') as Clear:
   #Clear.write("")
## clear.write("")

def check(distribution):# for the check of existeance of hospital
    while True:
        Hospital = {}
        with open("Hospitals.txt", "r") as Hos_File:
            for info in Hos_File:
                hospital_code, hospital_name, hospital_contact = info.strip().split("/")
                Hospital[hospital_code] = (hospital_name, hospital_contact)
            if distribution not in Hospital:
                print(info)
                print("not found hospital")
                distribution=input('confirm the hospital code again:')
                continue
            else:
                return distribution


def Hospital_Hospital():#hospital registration
    Hospital = {}

    with open("Hospitals.txt", "r") as Hos_File:
        hospital_code_add = input("Enter hospital code:")
        hospital_name_add = input("Enter hospital name:")
        hospital_contact_add = input("Enter hospital contact number")
        for info in Hos_File:
            hospital_code, hospital_name, hospital_contact = info.strip().split("/")
            Hospital[hospital_code] = (hospital_name, hospital_contact)

        if hospital_code_add in Hospital:
            print("Hospital already registered")
            return
        else:
            with open("Hospitals.txt", "a") as Hos_File:
                Hos_File.write(f"{hospital_code_add}/{hospital_name_add}/{hospital_contact_add}\n")
def distribution_total_quantity(distribution, item_to_update):#for tracking of supplier
    total_quantity = 0
    with open('Distribution.txt', 'r') as file:
        for line in file:
            item, dis,quantity_int = line.strip().split(',')
            quantity = int(quantity_int)
            if dis == distribution and item == item_to_update: #if in the same set of data
                total_quantity += quantity #quantity will added up

        return total_quantity
def Distribute(distribution,item_to_update, quantity):
    inventory = {}
    with open('ppe.txt', 'r') as File_inven:
        for var in File_inven:#check for existence of distribution
            item_code, supplier_code, item_quantity = var.strip().split("/")
            inventory[item_code] = (supplier_code, int(item_quantity))

    if item_to_update in inventory:
        with open("Distribution.txt", 'a') as Dis_file:
            Dis_file.write(f'{item_to_update},{distribution},{quantity}\n')


#################################################################################################################

def inventory_delete(item_code):
    with open('ppe.txt', 'r') as File_inven:
        info = File_inven.readlines()

    with open('ppe.txt', 'w') as File_inven:
        for information in info:
            var = information.strip().split("/")
            if var[0] != item_code:
                File_inven.write(information)
        print("Deletion done")


#################################################################################################################
def inventory_quantity(item_to_update, change, quantity):#inventory changes either distribute or receive to ppe
    inventory = {}
    with open('ppe.txt', 'r') as File_inven:
        for var in File_inven: #check for existence of ppe file
            item_code, supplier_code, item_quantity = var.strip().split("/")
            inventory[item_code] = (supplier_code, int(item_quantity))

    if item_to_update in inventory:
        if change == "+":
            Change_quantity = int(inventory[item_to_update][1]) + int(quantity)
            inventory[item_to_update] = (inventory[item_to_update][0], int(Change_quantity))
            with open('ppe.txt', 'w') as File_inven:
                for item_code, (supplier, item_quantity) in inventory.items():
                    File_inven.write(str(f'{item_code}/{supplier}/{int(item_quantity)}\n'))

                with open('ppe.txt', 'r') as File_inven:
                    inventory_list = File_inven.read()
                    print(inventory_list)#display updated inventory

                with open("Transaction.txt", 'a') as Transaction_file:
                    Transaction_file.write(f'{datetime.date.today()}:{inventory[item_to_update][0]}:{item_to_update}:{change}{quantity}\n')
                    print("update done")
        elif change == "-":
            distribution = input("what hospital is going to distributed to?:")
            check(distribution)
            Change_quantity = int(inventory[item_to_update][1]) - int(quantity)
            inventory[item_to_update] = (inventory[item_to_update][0], int(Change_quantity))
            Distribute( distribution,item_to_update, quantity)
            with open('ppe.txt', 'w') as File_inven:
                for item_code, (supplier_code, item_quantity) in inventory.items():
                    File_inven.write(str(f'{item_code}/{supplier_code}/{int(item_quantity)}\n'))

                with open('ppe.txt', 'r') as File_inven:
                    inventory_list = File_inven.read()
                    print(inventory_list)#display updated inventory

                with open("Transaction.txt", 'a') as Transaction_file:
                    Transaction_file.write(f'{datetime.date.today()}:{inventory[item_to_update][0]}:{item_to_update}:{change}{quantity}\n')
                    print("update done")




        else:
            print("follow instruction")



    #################################################################################################################
def inventory_record(item_code,supplier_code_add,item_quantity):#add new item
    with open('ppe.txt', "a") as File_inven:
        File_inven.write(f'{item_code}/{supplier_code_add}/{item_quantity}\n')


    with open("Transaction.txt", 'a') as Transaction_file:
        Transaction_file.write(f'{datetime.date.today()}:{supplier_code_add}:{item_code}:+{item_quantity}\n')

#################################################################################################################
def inventory_search(item_code):#use item code to search item
    with open('ppe.txt', "r") as File_inven:
        information = File_inven.readlines()
        for info in information:
            var = info.strip().split("/")
            if item_code == var[0]:
                print(info)


#################################################################################################################

def calculate_total_quantity(start_date, end_date, item_code):#tracking the quantity of specific item
    total_quantity = 0
    with open('Transaction.txt', 'r') as file:
        for line in file:
            date,sup,code, quantity_int = line.strip().split(':')
            quantity = int(quantity_int)
            if start_date <= date <= end_date and code == item_code: #item quantity within this range will be summed up
                total_quantity += quantity

    return total_quantity



def inventory():

#################################################################################################################
    while True:

        with open("ppe.txt", 'r') as File_inven:# display whole inventory file
            inventory = {}
            print("Inventory\n")
            print("Item Code/Supplier Code/Quantity")
            for var in File_inven:
                item_code, supplier_code, item_quantity = var.strip().split("/")
                inventory[item_code] = (supplier_code, int(item_quantity))
                print(var)
        with open("ppe.txt",'r') as File_inven:# notify low quantity item ,read again as noification do not print out during displaying inventory list
            for var in File_inven:
                item_code, supplier_code, item_quantity = var.strip().split("/")
                if inventory[item_code][1] <= 25:
                    print(f"{item_code} quantity alert !!! quantity left:{inventory[item_code][1]}")

        print("*" * 20)
        choice=input("insert 1 to search inventory, insert 2 to update new item,insert 3 to update quantity of item,insert 4 to delete item,insert 5 to track transaction,6 to track Distrbution:")
        if choice == "1" :#
            item_code=input("item code")
            inventory_search(item_code)
            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break##back to  menu

        elif choice=="2":#add supplier
            item_code = input("item code").strip()
            item_quantity=int(input("item quantity"))
            supplier_code_add = input("sup code")

            Supplier.supplier_detail_update(supplier_code_add)#call function
            inventory_record(item_code,supplier_code_add,item_quantity)

            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break#back to inventory menu

        elif choice =="3":#item changes receive to ppe or distribute


            item_to_update = input("Item code to distribute or received to PPE Storage")
            change = input("If need to receive press '+' if need to distribute press'-'")
            quantity = int(input("enter quantity that wanted to Received or Distribute:"))


            if change=="-":#distribute
                with open("ppe.txt", 'r') as quan_check:
                    inventory = {}
                    for var in quan_check:
                        item_code, supplier_code, item_quantity = var.strip().split("/")
                        inventory[item_code] = (supplier_code, int(item_quantity))
                    if item_to_update in inventory:
                        inventory[item_to_update] = (inventory[item_to_update][0],inventory[item_to_update][1])
                        with open("ppe.txt", 'r') :
                            if int(inventory[item_to_update][1])<int(quantity):
                                print(f'quantity is {inventory[item_to_update][1]} for item {item_to_update}')
                                return False
                            else:
                                pass
                    inventory_quantity(item_to_update, change, quantity)#call function
            if change=="+" :#receive
                inventory_quantity(item_to_update, change, quantity)#call function
            elif change=="-":
                pass
            else:
                print("please use + or -")



            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to menu
            elif Back_to_menu == "E":
                break#terminate program

        elif choice =="4":#search for item code
            item_code=input("item code")

            inventory_delete(item_code)

            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break#back to menu

        elif choice == "5":#track transaction
            start_date = input("Enter the start date (YYYY-MM-DD): ").strip()
            end_date = input("Enter the end date (YYYY-MM-DD): ").strip()
            item_code = input("Enter the item code: ").strip()
            total_quantity=calculate_total_quantity(start_date, end_date, item_code)
            print(f'Total quantity of item {item_code} between {start_date} and {end_date}: {total_quantity}')
            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break#back to menu

        elif choice == "6":#track distribution
            distribution = input("hospital code")
            item_to_update = input("Enter the item code:")
            print(f"the total number of item that this distributed to this hospital:{distribution_total_quantity(distribution, item_to_update)}")
            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break#back to menu

        else:#if variable choice is not prompted properly
            print("follow the instruction")
            print("*" * 20)
            Back_to_menu = input("If wanted to continue inventory press C /If wanted to exit inventory press E").strip()
            if Back_to_menu == "C":
                continue#back to inventory menu
            elif Back_to_menu == "E":
                break#back to  menu

