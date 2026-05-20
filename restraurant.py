import datetime as dt
from ctypes import c_double

def get_date():
    a = dt.date.today()
    x = str(a.day) if a.day>=10 else ("0" + str(a.day))
    y = str(a.month) if a.month>=10 else ("0" + str(a.month))
    z = str(a.year)
    return x + "-" + y + "-" + z

def get_total(req_date):
    fobj = open("all_bills.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()
    bill_total = 0

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[1] == req_date:
            bill_total = bill_total + int( ls[2][0:len(ls[2])-1] )
    return bill_total

def get_next_number(fname):
    fobj = open(fname, "r")
    all_lines = fobj.readlines()
    fobj.close()
    return len(all_lines) + 1

def get_dish_info(code):
    fobj = open("all_dish.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()
    dish_found = False

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[0] == code:
            dname = ls[1]
            dprice = ls[2][0:len(ls[2])-1 ]
            dish_found = True
            break

    if dish_found == True:
        return dname,dprice
    elif dish_found == False:
        return False,False

def create_new_bill():
    total_bill_amount = 0
    while True:
        dish_code = input("Enter DISH CODE or 0 to complete the Bill : ")
        if dish_code != "0":
            n,p = get_dish_info(dish_code)
            if n==False:
                print("Invalid Dish Code")
                continue
            else:
                q = int( input("Enter Quantity for " + n + " : ") )
                tot = q * int(p)
                total_bill_amount = total_bill_amount + tot
                print("Added..")
                continue
        elif dish_code == "0":
            bill_num = str( get_next_number("all_bills.txt") )
            bill_date = get_date()
            fobj = open("all_bills.txt", "a")
            fobj.write(bill_num + "," + bill_date + "," + str(total_bill_amount) + "\n")
            fobj.close()
            print("Total Bill Amount : ", total_bill_amount)
            break
    input()

def view_all_dish():
    fobj = open("all_dish.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    for oneline in all_lines:
        ls = oneline.split(",")
        print(ls[0], ls[1], ls[2], sep="\t", end="")
    input()

def update_dish_price():
    # similar to "return Book" logic
    pass

def add_new_dish():
    d_code = str( get_next_number("all_dish.txt") )
    d_name = input("Enter Dish Name : ")
    d_price = input("Enter Dish Price : ")

    fobj = open("all_dish.txt", "a")
    fobj.write(d_code + "," + d_name + "," + d_price + "\n")
    fobj.close()
    print("New Dish Added...")
    input()

def view_todays_collection():
    today = get_date()
    tot = get_total(today)
    print("Today's Total collection : ", tot)
    input()

def view_collection_on_date():
    any_date = input("Enter Date in DD-MM-YYYY form : ")
    tot = get_total(any_date)
    print("Total Collection on", any_date, "is : ", tot)
    input()

def view_collection_between_dates():
    fobj = open("all_bills.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    st_date = input("Enter Start Date in DD-MM-YYYY format : ")
    end_date = input("Enter End Date in DD-MM-YYYY format : ")
    tot_bill = 0

    for oneline in all_lines:
        ls = oneline.split(",")
        if ls[1]>=st_date and ls[1]<=end_date:
            tot_bill = tot_bill + int( ls[2][0:len(ls[2])-1 ] )
    print("Total Collection from", st_date, "to", end_date, "is : ", tot_bill)
    input()

# execution starts from here
fobj1 = open("all_dish.txt", "a")
fobj1.close()
fobj2 = open("all_bills.txt", "a")
fobj2.close()

while True:
    print("Select Operation")
    print("1 - Create New Bill")
    print("2 - View All Dish")
    print("3 - Update Dish Price")
    print("4 - Add New Dish")
    print("5 - View Today's Collection")
    print("6 - View Collection on Date")
    print("7 - View Collection Between Dates")
    print("8 - Exit")
    ch = int(input("Provide your choice : ") )
    if ch==1: create_new_bill()
    elif ch==2: view_all_dish()
    elif ch==3: update_dish_price()
    elif ch==4: add_new_dish()
    elif ch==5: view_todays_collection()
    elif ch==6: view_collection_on_date()
    elif ch==7: view_collection_between_dates()
    elif ch==8: exit(0)
