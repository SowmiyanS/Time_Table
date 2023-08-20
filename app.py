#TimeTable
#Generate time table based on the user's inputs
#Run the program answer the questions asked by it
#The time table is displayed finally
shop_time1=0
shop_time2=0
shop_time3=0
def fetch_water() :
    global Fetch_water
    print("Enter 'yes' (y) or 'no' (n)")
    F_w = str(input("Fetch_water is true : "))
    if (F_w == 'y') :
        Fetch_water = True 
        print("Copied")
    elif (F_w == 'n') :
        Fetch_water = False
        print("Copied")
    else :
        print("You entered wrong string!! || enter y/n")
        fetch_water()
def go_shop() :
    global Go_shop
    G_s = str(input("Go_shop is true : ")) 
    if (G_s == 'y') :
        Go_shop = True
        print("Copied")
    elif (G_s == 'n') :
        Go_shop = False
        print("Copied")
    else :
        print("You entered wrong string!! || enter y/n")
        go_shop()
def get_shop_time() :
    global shop_time1
    global shop_time2
    global shop_time3
    s_m = int(input("Enter number of times of shop : "))
    if (s_m > 0 ) :
        s_m =s_m-1
        G_t = int(input("Enter time as int : "))
        print("Enter 'am' or 'pm'")
        Session = str(input("Enter the session : "))
        if (Session == 'am') :
            G_t =G_t + 0
            shop_time1 = G_t
            print("Copied")
        elif (Session == 'pm') :
            G_t =G_t + 12
            shop_time1 = G_t
            print("Copied")
        else :
            print("You entered wrong!!")
            get_shop_time()
        if (s_m > 0):
            s_m = s_m -1
            G_t = int(input("Enter time as int : "))
            print("Enter 'am' or 'pm' ")
            Session = str(input("Enter the session : "))
            if (Session == 'am') :
                G_t = G_t + 0
                shop_time2 = G_t
                print("Copied")
            elif (Session == 'pm') :
                G_t = G_t + 12
                shop_time2 = G_t
                print("Copied")
            else :
                print("you entered wrong!!")
                get_shop_time()
            if (s_m > 0) :
                s_m = s_m -1
                G_t = int(input("Enter time as int : "))
                print("Enter 'am' or 'pm' ")
                Session = str(input("Enter the session"))
                if (Session == 'am'):
                    G_t = G_t + 0
                    shop_time3 = G_t
                    print("Copied")
                elif (Session == 'pm') :
                    G_t = G_t + 12
                    shop_time3 = G_t
                    print("Copied")
                else :
                    print("you entered wrong!!")
                    get_shop_time()  
    elif (s_m <= 0) :
        pass
    else :
        print("You entered wrong!!")
        get_shop_time()
def bath() :
    global Bath
    B = str(input("Bath is true : "))
    if (B == 'y')  :
        Bath = True
        print("Copied") 
    elif (B == 'n') :
        Bath = False
        print("Copied")
    else :
        print("You entered wrong string!! || enter y/n")
        bath()
def PRINT():
    print("__________________________________________")
    print("|      TIME        "+"   |   "+"    WORK       |")
    print("|_____________________|__________________|")
    print("|  7:00 - 8:00  AM"+"    |   "+Alpha[7]+"  |")
    print("|_____________________|__________________|")
    print("|  8:00 - 9:00   AM"+"   |   "+Alpha[8]+"  |")
    print("|_____________________|__________________|")
    print("|  9:00 - 10:00  AM"+"   |   "+Alpha[9]+"  |")
    print("|_____________________|__________________|")
    print("|  10:00 - 11:00  AM"+"  |   "+Alpha[10]+"  |")
    print("|_____________________|__________________|")
    print("|  11:00 - 12:00  AM"+"  |   "+Alpha[11]+"  |")
    print("|_____________________|__________________|")
    print("|  12:00 - 1:00  PM"+"   |   "+Alpha[12]+"  |")
    print("|_____________________|__________________|")
    print("|  1:00 - 2:00  PM"+"    |   "+Alpha[13]+"  |")
    print("|_____________________|__________________|")
    print("|  2:00 - 3:00  PM"+"    |   "+Alpha[14]+"  |")
    print("|_____________________|__________________|")
    print("|  3:00 - 4:00  PM"+"    |   "+Alpha[15]+"  |")
    print("|_____________________|__________________|")
    print("|  4:00 - 5:00  PM"+"    |   "+Alpha[16]+"  |")
    print("|_____________________|__________________|")
    print("|  5:00 - 6:00  PM"+"    |   "+Alpha[17]+"  |")
    print("|_____________________|__________________|")
    print("|  6:00 - 7:00  PM"+"    |   "+Alpha[18]+"  |")
    print("|_____________________|__________________|")
    print("|  7:00 - 8:00  PM"+"    |   "+Alpha[19]+"  |")
    print("|_____________________|__________________|")
    print("|  8:00 - 9:00  PM"+"    |   "+Alpha[20]+"  |")
    print("|_____________________|__________________|")
    print("|  9:00 - 10:00  PM"+"   |   "+Alpha[21]+"  |")
    print("|_____________________|__________________|")
# program starts from here
import random
fetch_water()  
go_shop()
if (Go_shop == True):
    get_shop_time()
bath()
Alpha={7:'a',8:'b',9:'c',10:'d',11:'e',12:'f',13:'g',14:'h',15:'i',16:'j',17:'k',18:'l',19:'m',20:'n',21:'o' }
N_eight_list=["Entertainment","   Gaming    ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   "]
N_n_list=["Entertainment","   Gaming    ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   "]
N_ten_list=["Entertainment","   Gaming    ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   "]
N_eleven_list=["Entertainment","   Gaming    ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   ","   YouTube   "]
if (Fetch_water == True):
    if (Go_shop == True):
        if(Bath == True):
            random.shuffle(N_eight_list)
            Alpha[7]=" Fetch water "
            Alpha[8]=" Fetch water "
            Alpha[9]="    Bath     "
            Alpha[10]="  Breakfast  "
            Alpha[11]=N_eight_list[0]
            Alpha[13]="    Lunch    "
            Alpha[12]=N_eight_list[1]
            Alpha[14]=N_eight_list[2]
            Alpha[16]="    Lunch    "
            Alpha[15]=N_eight_list[3]
            Alpha[17]=N_eight_list[4]
            Alpha[18]=N_eight_list[5]
            Alpha[20]="   Dinner    "
            Alpha[19]=N_eight_list[6]
            Alpha[21]=N_eight_list[7]
            Alpha[int(shop_time1)]="   Go shop   "
            Alpha[int(shop_time2)]="   Go shop   "
            Alpha[int(shop_time3)]="   Go shop   "
            if (shop_time1==7 or shop_time1==8 or shop_time1==9 or shop_time1==10 or shop_time1==13 or shop_time1==16 or shop_time1==20 or shop_time2==7 or shop_time2==8 or shop_time2==9 or shop_time2==10 or shop_time2==13 or shop_time2==16 or shop_time2==20 or shop_time3==7 or shop_time3==8 or shop_time3==9 or shop_time3==10 or shop_time3==13 or shop_time3==16 or shop_time3==20):
                print("You are trying to Go shop during unexpected times, Reenter!")
            else:
                PRINT()
        else:
            random.shuffle(N_n_list)
            Alpha[7]=" Fetch water "
            Alpha[8]=" Fetch water "
            Alpha[9]="  Breakfast  "
            Alpha[10]=N_n_list[0]
            Alpha[11]=N_n_list[1]
            Alpha[13]="    Lunch    "
            Alpha[12]=N_n_list[2]
            Alpha[14]=N_n_list[3]   
            Alpha[16]="    Lunch    "
            Alpha[15]=N_n_list[4]
            Alpha[17]=N_n_list[5]
            Alpha[18]=N_n_list[6]
            Alpha[20]="   Dinner    "
            Alpha[19]=N_n_list[7]
            Alpha[21]=N_n_list[8]
            Alpha[int(shop_time1)]="   Go shop   "
            Alpha[int(shop_time2)]="   Go shop   "
            Alpha[int(shop_time3)]="   Go shop   "
            if (shop_time1==7 or shop_time1==8 or shop_time1==9 or shop_time1==13 or shop_time1==16 or shop_time1==20 or shop_time2==7 or shop_time2==8 or shop_time2==9 or shop_time2==13 or shop_time2==16 or shop_time2==20 or shop_time3==7 or shop_time3==8 or shop_time3==9 or shop_time3==13 or shop_time3==16 or shop_time3==20):
                print("You are trying to Go shop during unexpected times, Reenter!")
            else:
                PRINT()
    else:
        if (Bath == True):
            Alpha[7]=" Fetch water "
            Alpha[8]=" Fetch water "
            Alpha[9]="    Bath     "
            Alpha[10]="  Breakfast  "
            Alpha[11]=N_eight_list[0]
            Alpha[13]="    Lunch    "
            Alpha[12]=N_eight_list[1]
            Alpha[14]=N_eight_list[2]
            Alpha[16]="    Lunch    "
            Alpha[15]=N_eight_list[3]
            Alpha[17]=N_eight_list[4]
            Alpha[18]=N_eight_list[5]
            Alpha[20]="   Dinner    "
            Alpha[19]=N_eight_list[6]
            Alpha[21]=N_eight_list[7]
            PRINT()
        else:
            random.shuffle(N_n_list)
            Alpha[7]=" Fetch water "
            Alpha[8]=" Fetch water "
            Alpha[9]="  Breakfast  "
            Alpha[10]=N_n_list[0]
            Alpha[11]=N_n_list[1]
            Alpha[13]="    Lunch    "
            Alpha[12]=N_n_list[2]
            Alpha[14]=N_n_list[3]   
            Alpha[16]="    Lunch    "
            Alpha[15]=N_n_list[4]
            Alpha[17]=N_n_list[5]
            Alpha[18]=N_n_list[6]
            Alpha[20]="   Dinner    "
            Alpha[19]=N_n_list[7]
            Alpha[21]=N_n_list[8]
            PRINT()
else:
    if (Go_shop == True):
        if (Bath == True):
            random.shuffle(N_ten_list)
            Alpha[7]=N_ten_list[0]
            Alpha[8]=N_ten_list[1]
            Alpha[9]="    Bath     "
            Alpha[10]="  Breakfast  "
            Alpha[11]=N_ten_list[2]
            Alpha[12]=N_ten_list[3]
            Alpha[13]="    Lunch    "
            Alpha[14]=N_ten_list[4]
            Alpha[15]=N_ten_list[5]
            Alpha[16]="    Lunch    "
            Alpha[17]=N_ten_list[6]
            Alpha[18]=N_ten_list[7]
            Alpha[19]=N_ten_list[8]
            Alpha[20]="   Dinner    "
            Alpha[21]=N_ten_list[9]
            Alpha[int(shop_time1)]="   Go shop   "
            Alpha[int(shop_time2)]="   Go shop   "
            Alpha[int(shop_time3)]="   Go shop   "
            if (shop_time1 ==9 or shop_time1==10 or shop_time1==13 or shop_time1==16 or shop_time1==20 or shop_time2==9 or shop_time2==10 or shop_time2==13 or shop_time2==16 or shop_time2==20 or shop_time3==9 or shop_time3==10 or shop_time3==13 or shop_time3==16 or shop_time3==20):
                print("You are trying to Go shop during unexpected times, Reenter!")
            else:
                PRINT()
        else:
            random.shuffle(N_eleven_list)
            Alpha[7]=N_eleven_list[0]
            Alpha[8]=N_eleven_list[1]
            Alpha[9]="  Breakfast  "
            Alpha[10]=N_eleven_list[2]
            Alpha[11]=N_eleven_list[3]
            Alpha[12]=N_eleven_list[4]
            Alpha[13]="    Lunch    "
            Alpha[14]=N_eleven_list[5]
            Alpha[15]=N_eleven_list[6]
            Alpha[16]="    Lunch    "
            Alpha[17]=N_eleven_list[7]
            Alpha[18]=N_eleven_list[8]
            Alpha[19]=N_eleven_list[9]
            Alpha[20]="   Dinner    "
            Alpha[21]=N_eleven_list[10]
            Alpha[int(shop_time1)]="   Go shop   "
            Alpha[int(shop_time2)]="   Go shop   "
            Alpha[int(shop_time3)]="   Go shop   "
            if (shop_time1 ==9 or shop_time1==13 or shop_time1==16 or shop_time1==20 or shop_time2==9 or shop_time2==13 or shop_time2==16 or shop_time2==20 or shop_time3==9 or shop_time3==13 or shop_time3==16 or shop_time3==20):
                print("You are trying to Go shop during unexpected times, Reenter!")
            else:
                PRINT()
    else:
        if (Bath == True):
            random.shuffle(N_eleven_list)
            Alpha[7]=N_ten_list[0]
            Alpha[8]=N_ten_list[1]
            Alpha[9]="    Bath     "
            Alpha[10]="  Breakfast  "
            Alpha[11]=N_ten_list[2]
            Alpha[12]=N_ten_list[3]
            Alpha[13]="    Lunch    "
            Alpha[14]=N_ten_list[4]
            Alpha[15]=N_ten_list[5]
            Alpha[16]="    Lunch    "
            Alpha[17]=N_ten_list[6]
            Alpha[18]=N_ten_list[7]
            Alpha[19]=N_ten_list[8]
            Alpha[20]="   Dinner    "
            Alpha[21]=N_ten_list[9]
            PRINT()
        else:        
            random.shuffle(N_eleven_list)
            Alpha[7]=N_eleven_list[0]
            Alpha[8]=N_eleven_list[1]
            Alpha[9]="  Breakfast  "
            Alpha[10]=N_eleven_list[2]
            Alpha[11]=N_eleven_list[3]
            Alpha[12]=N_eleven_list[4]
            Alpha[13]="    Lunch    "
            Alpha[14]=N_eleven_list[5]   
            Alpha[15]=N_eleven_list[6]
            Alpha[16]="    Lunch    "
            Alpha[17]=N_eleven_list[7]
            Alpha[18]=N_eleven_list[8]
            Alpha[19]=N_eleven_list[9]
            Alpha[20]="   Dinner    "
            Alpha[21]=N_eleven_list[10]
            PRINT() 

