#TEO HUI BIN, HOUNG YEW LIANG
#TP075611,TP074471
#Program Author
def supplier_detail_update(supplier_code_add): #adding new supplier detail
    supplier = {}
    with open("supplier.txt", 'r') as Sup_file:#read supplier file
        for info in Sup_file:
            supplier_code, Supplier_name, Supplied_item=info.strip().split("/")
            supplier[supplier_code] = (Supplier_name, Supplied_item)
        Supplied_item_add = input("sup item")
        if Supplied_item_add not in supplier:#if item is new
            Supplier_name = input("sup name")
            with open("supplier.txt",'a') as Sup_file:
                Sup_file.write(f'{supplier_code_add}/{Supplier_name}/{Supplied_item_add}\n')
        else: #if founded same item, will not write in file
            pass


def supplier_detail_read():#read supplier information and display
    with open("supplier.txt", 'r') as Sup_file:
        Sup_info = Sup_file.readlines()
        for info in Sup_info:
            Sup = info.strip().split("/")
            print(Sup)

def supplier_detail_search(Supplier_code_search,Supplier_name,Supplied_item):#read supplier information
    supplier = {}
    with open("supplier.txt", 'r') as Sup_file:
        Sup_info = Sup_file.readlines()
        for info in Sup_info:
            supplier_code,Supplier_name,Supplied_item= info.strip().split("/")
            supplier[supplier_code] = (Supplier_name, Supplied_item)

    if Supplier_code_search in supplier: #use prompted to find targeted supplier
        supplier[Supplier_code_search] = (Supplier_name, Supplied_item)
        print(supplier[Supplier_code_search]) # print when founded

def supplier_delete(supplier_code): #delete supplier detail
    with open('supplier.txt','r') as File_inven:
        info=File_inven.readlines()
        with open('supplier.txt','w') as File_inven:
            for information in info:
                var=information.strip().split("/")
                if var[0]!=supplier_code:#write all detail execept the targeted supplier
                    File_inven.write(information)




