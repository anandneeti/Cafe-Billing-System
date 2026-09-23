from tkinter import *
from tkinter import messagebox
import random,os
root=Tk()
root.title('Cafe Billing System')
root.geometry('1276x685')

newbillno=1
def billno():
    global newbillno
    file_exists = os.path.isfile('lastbillno.txt')
    if file_exists:
            f=open("lastbillno.txt",'r+')
            s = f.read().strip()
            newbillno=int(s)+1
            f.seek(0)            
            f.write(str(newbillno))
            f.truncate()
            f.close()
    else:
        f=open("lastbillno.txt",'w')
        f.write(str(newbillno))
        f.close()

if not os.path.exists('bills'):
    os.mkdir('bills')

def is_numeric(a):
    if a.isdigit():
        return True
    else:
        messagebox.showerror('ERROR!', 'You have certainly entered non-numeric values in certain quantity boxes. Make sure to enter numeric values only!!')
        return False
def is_valid_phno(b):
    valid=True
    if len(b)==10:
        for i in b:
            if i.isdigit():
                pass
            else:
                valid=False
                break
    else:
        valid=False
    if valid==False:
        messagebox.showerror("ERROR!","The phone number entered is not a valid one!")
        return False
    return True

def searchbill(a):
    file_path = os.path.join("bills", f" {a}.txt")
    file_exists = os.path.isfile(file_path)
    if file_exists:
        def display_bill(bill_no, content):
            bill_window = Toplevel(root)
            bill_window.title(f"Bill No: {a}")
            bill_window.geometry("500x400")

            # Text area to display the bill content
            textarea = Text(bill_window, wrap='word', font=('times new roman', 12),height=8)
            textarea.pack(expand=True, fill='both')
            textarea.insert('1.0', content)

            # Button to close the bill window
            close_button = Button(bill_window, text="Close", command=bill_window.destroy)
            close_button.pack()

        with open(file_path,'r') as file:
            s=file.read()
            display_bill(f"{a}", s)
            file.close()
    else:
        messagebox.showinfo("No bill found",f"No bill with bill no. {a} found.")


def savebill():
    global newbillno
    result=messagebox.askyesno('CONFIRM','DO YOU WANT TO SAVE THE BILL?')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {newbillno}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('SUCCESS',f'BILLNO:{newbillno} SAVED SUCCESSFULLY')
        

def clear():
    capuccinoentry.delete(0,END)
    americanoentry.delete(0,END)
    espressoentry.delete(0,END)
    macchiatoentry.delete(0,END)
    latteentry.delete(0,END)
    sandwichentry.delete(0,END)
    donutentry.delete(0,END)
    friesentry.delete(0,END)
    burgerentry.delete(0,END)
    brentry.delete(0,END)
    mpentry.delete(0,END)
    cakeentry.delete(0,END)
    pastryentry.delete(0,END)
    pancakeentry.delete(0,END)
    truffleentry.delete(0,END)
    crentry.delete(0,END)
    ccentry.delete(0,END)
    
    capuccinoentry.insert(0,0)
    americanoentry.insert(0,0)
    espressoentry.insert(0,0)
    macchiatoentry.insert(0,0)
    latteentry.insert(0,0)
    sandwichentry.insert(0,0)
    donutentry.insert(0,0)
    friesentry.insert(0,0)
    burgerentry.insert(0,0)
    brentry.insert(0,0)
    mpentry.insert(0,0)
    cakeentry.insert(0,0)
    pastryentry.insert(0,0)
    pancakeentry.insert(0,0)
    truffleentry.insert(0,0)
    crentry.insert(0,0)
    ccentry.insert(0,0)
    
    bevpriceentry.delete(0,END)
    snackspriceentry.delete(0,END)
    dessertspriceentry.delete(0,END)

    nameentry.delete(0,END)
    phentry.delete(0,END)
    billnoentry.delete(0,END)
    textarea.delete(1.0,END)
    
import csv
from tkinter import END
totalbevprice,totalsnacksprice,totaldessertsprice=0,0,0
d = {}      # Initialize dictionary to store item prices from CSV
d1={}       # Dictionary to store prices of different items as separate variables
def check_qty():
    if is_numeric(mpentry.get()):
        pass
    else:
        return
    if is_numeric(brentry.get()):
        pass
    else:
        return
    if is_numeric(capuccinoentry.get()):
        pass
    else:
        return
    if is_numeric(americanoentry.get()):
        pass
    else:
        return
    if is_numeric(teaentry.get()):
        pass
    else:
        return
    if is_numeric(latteentry.get()):
        pass
    else:
        return
    if is_numeric(macchiatoentry.get()):
        pass
    else:
        return
    if is_numeric(pancakeentry.get()):
        pass
    else:
        return
    if is_numeric(donutentry.get()):
        pass
    else:
        return
    if is_numeric(friesentry.get()):
        pass
    else:
        return
    if is_numeric(burgerentry.get()):
        pass
    else:
        return
    if is_numeric(truffleentry.get()):
        pass
    else:
        return
    if is_numeric(crentry.get()):
        pass
    else:
        return
    if is_numeric(ccentry.get()):
        pass
    else:
        return
    if is_numeric(pastryentry.get()):
        pass
    else:
        return
    if is_numeric(cakeentry.get()):
        pass
    else:
        return
    if is_numeric(espressoentry.get()):
        pass
    else:
        return
    if is_numeric(sandwichentry.get()):
        pass
    else:
        return
    return True
def total():
    global totalbevprice,totalsnacksprice,totaldessertsprice
    global d,d1
    #Check if quantity entered is valid or not
    if check_qty():
        pass
    else:
        return
    # Open the CSV file once and read its contents
    try:
        with open("ITEM PRICES.csv", 'r') as f1:
            csvob = csv.reader(f1, delimiter=",")
            for row in csvob:
                # Assuming the CSV structure is: ItemName, ItemPrice
                d[row[0]] = int(row[1])  # Store prices as integers
    except FileNotFoundError:
        print("CSV file not found. Please check the file path.")
        return
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Define a list of items and their respective Tkinter entry variables
    t = [
    [capuccinoentry, 'Capuccino', 'capuccinovalue'],
    [americanoentry, 'Americano', 'americanovalue'],
    [espressoentry, 'Espresso', 'espressovalue'],
    [teaentry, 'Tea', 'teavalue'],
    [macchiatoentry, 'Macchiato', 'macchiatovalue'],
    [latteentry, 'Latte', 'lattevalue'],
    [sandwichentry, 'Sandwich', 'sandwichvalue'],
    [donutentry, 'Donnuts', 'donutvalue'],
    [friesentry, 'Fries', 'friesvalue'],
    [burgerentry, 'Burger', 'burgervalue'],
    [brentry, 'Bread Roll', 'brvalue'],
    [mpentry, 'Mcpuff', 'mpvalue'],
    [cakeentry, 'Cake', 'cakevalue'],
    [pastryentry, 'Pastry', 'pastryvalue'],
    [pancakeentry, 'Pancakes', 'pancakevalue'],
    [truffleentry, 'Strawberry Truffle', 'trufflevalue'],
    [crentry, 'Cream Roll', 'crvalue'],
    [ccentry, 'Cupcake', 'ccvalue']
]

    # Initialize total price variables for each category
    totalbevprice = 0
    totalsnacksprice = 0
    totaldessertsprice = 0

    # Categories to classify items
    beverage_items = ['Capuccino', 'Americano', 'Espresso', 'Tea', 'Macchiato', 'Latte']
    snack_items = ['Sandwich', 'Donnuts', 'Fries', 'Burger', 'Bread Roll', 'Mcpuff']
    dessert_items = ['Cake', 'Pastry', 'Pancakes', 'Strawberry Truffle', 'Cream Roll', 'Cupcake']


    # Loop through the items and calculate the total prices based on user input
    for entry_value, item_name,item_pricevalue in t:
        quantity = entry_value.get() or '0'  # Default to '0' if no input
        quantity = int(quantity)  # Convert to integer
        if quantity > 0:  # Only process if quantity is greater than 0
            if item_name in d:
                price = d[item_name] * quantity
                d1[item_pricevalue]=price  
                # Add to appropriate category
                if item_name in beverage_items:
                    totalbevprice += price
                elif item_name in snack_items:
                    totalsnacksprice += price
                elif item_name in dessert_items:
                    totaldessertsprice += price

    # Update the Tkinter entry fields with the calculated total prices
    bevpriceentry.delete(0, END)
    bevpriceentry.insert(0, f'{totalbevprice} Rs.')

    snackspriceentry.delete(0, END)
    snackspriceentry.insert(0, f'{totalsnacksprice} Rs.')

    dessertspriceentry.delete(0, END)
    dessertspriceentry.insert(0, f'{totaldessertsprice} Rs.')

    # Calculate the total bill
    totalbill = totalbevprice + totalsnacksprice + totaldessertsprice
    
def bill():
    # Check if valid customer details are entered
    if nameentry.get() == '' or phentry.get() == '':
        messagebox.showerror('Error', 'Customer details are required')
        return                                                                                  # Exit the function if details are missing
    #Check if valid phone number is entered
    if is_valid_phno(phentry.get()):            
        pass
    else:
        return
    # Check if no valid products are selected 
    if bevpriceentry.get() == '0 Rs.' and snackspriceentry.get() == '0 Rs.' and dessertspriceentry.get() == '0 Rs.':
        messagebox.showerror('Error', 'No Products are selected')
        return
    #Check if quantity entered is valid or not
    if check_qty():
        pass
    else:
        return

    # Constructing the bill
    textarea.delete(1.0,END)
    billno()
    textarea.insert(END, '\t\t*WELCOME TO THE CAFE CUSTOMER*\n')
    textarea.insert(END, f'\nBILL NO.: {newbillno}\n\n')
    textarea.insert(END, f'CUSTOMER NAME: {nameentry.get()}\n\n')
    textarea.insert(END, f'PHONE NO.: {phentry.get()}\n\n')
    textarea.insert(END, '=======================================================\n')
    textarea.insert(END, 'PRODUCT\t\tQUANTITY\t\tUNIT PRICE\t\tPRICE\n')
    textarea.insert(END, '=======================================================\n')

    # Function to insert item details into the bill if quantity is greater than or equal to 1
    def insert_item(entry, item_name, value):
        quantity = entry.get()
        if quantity != '' and int(quantity) >= 1:
            textarea.insert(END, f'{item_name}\t\t{quantity.lstrip("0")}\t\t{d[item_name]}\t\t{d1[value]} Rs.\n')

    # Insert each item and its details if the quantity is valid (>= 1)
    insert_item(capuccinoentry, 'Capuccino', 'capuccinovalue')
    insert_item(americanoentry, 'Americano', 'americanovalue')
    insert_item(espressoentry, 'Espresso', 'espressovalue')
    insert_item(teaentry, 'Tea', 'teavalue')
    insert_item(macchiatoentry, 'Macchiato','macchiatovalue')
    insert_item(latteentry, 'Latte', 'lattevalue')
    insert_item(sandwichentry, 'Sandwich', 'sandwichvalue')
    insert_item(donutentry, 'Donnuts', 'donutvalue')
    insert_item(friesentry, 'Fries', 'friesvalue')
    insert_item(burgerentry, 'Burger', 'burgervalue')
    insert_item(brentry, 'Bread Roll', 'brvalue')
    insert_item(mpentry, 'Mcpuff','mpvalue')
    insert_item(cakeentry, 'Cake','cakevalue')
    insert_item(pastryentry, 'Pastry', 'pastryvalue')
    insert_item(pancakeentry, 'Pancakes', 'pancakevalue')
    insert_item(truffleentry, 'Strawberry Truffle', 'trufflevalue')
    insert_item(crentry, 'Cream Roll', 'crvalue')
    insert_item(ccentry, 'Cupcake','ccvalue')

    # Calculate total bill
    totalbill = totalbevprice + totalsnacksprice + totaldessertsprice
    textarea.insert(END, f'\nGRAND TOTAL: {totalbill} Rs.')
    textarea.insert(END, '\n\nTHANK YOU... PLEASE VISIT US AGAIN!')
    textarea.insert(END, '\n=======================================================')
    
    # Save the bill
    savebill()


def get_price_from_csv(item_name, csv_file="ITEM PRICES.csv"):
    try:
        with open(csv_file, mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0]== item_name.strip():
                    return row[1]
    except FileNotFoundError:
        print(f"CSV file {csv_file} not found.")
        return "Price Not Found"
    file.close()

def exit_program():
    root.destroy()

def update():
    print("WELCOME TO THE CAFE MANAGEMENT APPLIATION")
    ans=input("Kindly confirm if you want to change prices of any item? (Y/N):")
    ans=ans.lower()
    while ans=="y":
        item=input("Enter name of item whose price you want to change:")
        file=open("ITEM PRICES.csv","r+",newline='')
        nfile=open("New.csv","w",newline='')
        csvobject=csv.reader(file)
        csvwriter=csv.writer(nfile)
        d=[]
        found=False
        for x in csvobject:
            if x[0].lower()==item.lower():
                found=True
        file.close()
        file=open("ITEM PRICES.csv","r+",newline='')
        csvobject=csv.reader(file)
        if found==True:
            for i in csvobject:
                if i[0].lower()==item.lower():
                    nprice=int(input("Enter new price:"))
                    q=[i[0],str(nprice)]
                    d.append(q)
                else:
                    q=[i[0],i[1]]
                    d.append(q)
            csvwriter.writerows(d)
            file_exists= os.path.isfile('ORIGINAL FILE.csv')
            file.close()
            nfile.close()
            if file_exists:
                os.remove("ORIGINAL FILE.csv")
            os.rename("ITEM PRICES.csv","ORIGINAL FILE.csv")
            os.rename("New.csv","ITEM PRICES.csv")
            print("Price updated successfully!")
        else:
            print("ITEM NOT FOUND!")
        ans=input("Do you want to change prices of any other item (Y/N):")
update()

#------------heading frame--------------------
headingLabel=Label(root,text='CAFE BILLING SYSTEM', font=('times new roman', 36, 'bold')
                   , bg='#061c32',fg='gold', bd=12, relief=GROOVE)
headingLabel.pack(fill=X,pady=10)


#---------------customer frame----------------------
customer_details_frame=LabelFrame(root, text='Customer Details',font=('times new roman', 15,'bold')
                                  , fg='gold', bd=8, relief=GROOVE, bg='#061c32')
customer_details_frame.pack(fill=X)
nameLabel=Label(customer_details_frame, text="Name", font=('times new roman', 15, 'bold'),bg='#061c32',
                fg='white')

#name label-----
nameLabel.grid(row=0,column=0, padx=20)
nameentry=Entry(customer_details_frame, font=('arial',15),bd=7, width=18)
nameentry.grid(row=0,column=1,padx=8)


#phone label-------
phlabel=Label(customer_details_frame, text='Phone Number',font=('times new roman',15,'bold'),bg='#061c32',
              fg='white')
phlabel.grid(row=0, column=2, padx=20, pady=2)
phentry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phentry.grid(row=0,column=3,padx=8)

#Bill no label-----
billnolabel=Label(customer_details_frame, text='Bill Number',font=('times new roman',15,'bold'),bg='#061c32',
              fg='white')
billnolabel.grid(row=0, column=4, padx=20, pady=2)
billnoentry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnoentry.grid(row=0,column=5,padx=8)

#search button------
searchbutton=Button(customer_details_frame,text='search',font=('arial',12,'bold'),command=lambda:searchbill(billnoentry.get()))
searchbutton.grid(row=0,column=6,padx=20)

#---------products frame------
productframe=Frame(root)
productframe.pack()

#beverages-------
bevframe=LabelFrame(productframe,text='Beverages', font=('times new roman',15,'bold'),fg='gold',
                    bd=8,relief=GROOVE,bg='#061c32')
bevframe.grid(row=0,column=0)

#capuccino
capuccinolabel=Label(bevframe, text='Capuccino', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
capuccinolabel.grid(row=0,column=0,sticky='w',padx=10)

capuccino_price = get_price_from_csv('Capuccino')
capuccinoprice_label = Label(bevframe, text=f' {capuccino_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
capuccinoprice_label.grid(row=0, column=1, sticky='w', padx=10)

capuccinoentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
capuccinoentry.grid(row=0,column=2,pady=9,padx=10)
capuccinoentry.insert(0,0)


#americano
americanolabel=Label(bevframe, text='Americano', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
americanolabel.grid(row=1,column=0,sticky='w',padx=10)

americano_price = get_price_from_csv('Americano')
americanoprice_label = Label(bevframe, text=f' {americano_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
americanoprice_label.grid(row=1, column=1, sticky='w', padx=10)

americanoentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
americanoentry.grid(row=1,column=2,pady=9,padx=10)
americanoentry.insert(0,0)


#espresso
espressolabel=Label(bevframe, text='Espresso', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
espressolabel.grid(row=2,column=0,sticky='w',padx=10)

espresso_price = get_price_from_csv('Espresso')
espressoprice_label = Label(bevframe, text=f' {espresso_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
espressoprice_label.grid(row=2, column=1, sticky='w', padx=10)

espressoentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
espressoentry.grid(row=2,column=2,pady=9,padx=10)
espressoentry.insert(0,0)


#tea
tealabel=Label(bevframe, text='Tea', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
tealabel.grid(row=3,column=0,sticky='w',padx=10)

tea_price = get_price_from_csv('Tea')
teaprice_label = Label(bevframe, text=f' {tea_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
teaprice_label.grid(row=3, column=1, sticky='w', padx=10)

teaentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
teaentry.grid(row=3,column=2,pady=9,padx=10)
teaentry.insert(0,0)


#macchiato
macchiatolabel=Label(bevframe, text='Macchiato', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
macchiatolabel.grid(row=4,column=0,sticky='w',padx=10)

macchiato_price = get_price_from_csv('Macchiato')
macchiatoprice_label = Label(bevframe, text=f' {macchiato_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
macchiatoprice_label.grid(row=4, column=1, sticky='w', padx=10)

macchiatoentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
macchiatoentry.grid(row=4,column=2,pady=9,padx=10)
macchiatoentry.insert(0,0)

#latte
lattelabel=Label(bevframe, text='Latte', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
lattelabel.grid(row=5,column=0,sticky='w',padx=10)

latte_price = get_price_from_csv('Latte')
latteprice_label = Label(bevframe, text=f' {latte_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
latteprice_label.grid(row=5, column=1, sticky='w', padx=10)

latteentry=Entry(bevframe,font=('times new roman',15,'bold'),width=3,bd=5)
latteentry.grid(row=5,column=2,pady=9,padx=10)
latteentry.insert(0,0)

#snacks-------
snacksframe=LabelFrame(productframe,text='Snacks', font=('times new roman',15,'bold'),fg='gold',
                    bd=8,relief=GROOVE,bg='#061c32')
snacksframe.grid(row=0,column=1)

#sandwich
sandwichlabel=Label(snacksframe, text='Sandwich', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
sandwichlabel.grid(row=0,column=0,sticky='w',padx=10)

sandwich_price = get_price_from_csv('Sandwich')
sandwichprice_label = Label(snacksframe, text=f' {sandwich_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
sandwichprice_label.grid(row=0, column=1, sticky='w', padx=10)

sandwichentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
sandwichentry.grid(row=0,column=2,pady=9,padx=10)
sandwichentry.insert(0,0)

#donuts
donutlabel=Label(snacksframe, text='Donnuts', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
donutlabel.grid(row=1,column=0,sticky='w',padx=10)

donut_price = get_price_from_csv('Donnuts')
donutprice_label = Label(snacksframe, text=f' {donut_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
donutprice_label.grid(row=1, column=1, sticky='w', padx=10)

donutentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
donutentry.grid(row=1,column=2,pady=9,padx=10)
donutentry.insert(0,0)

#fries
frieslabel=Label(snacksframe, text='Fries', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
frieslabel.grid(row=2,column=0,sticky='w',padx=10)

fries_price = get_price_from_csv('Fries')
friesprice_label = Label(snacksframe, text=f' {fries_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
friesprice_label.grid(row=2, column=1, sticky='w', padx=10)

friesentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
friesentry.grid(row=2,column=2,pady=9,padx=10)
friesentry.insert(0,0)

#burger
burgerlabel=Label(snacksframe, text='Burger', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
burgerlabel.grid(row=3,column=0,sticky='w',padx=10)

burger_price = get_price_from_csv('Burger')
burgerprice_label = Label(snacksframe, text=f' {burger_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
burgerprice_label.grid(row=3, column=1, sticky='w', padx=10)

burgerentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
burgerentry.grid(row=3,column=2,pady=9,padx=10)
burgerentry.insert(0,0)

#breadroll
brlabel=Label(snacksframe, text='Bread Roll', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
brlabel.grid(row=4,column=0,sticky='w',padx=10)

br_price = get_price_from_csv('Bread Roll')
brprice_label = Label(snacksframe, text=f' {br_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
brprice_label.grid(row=4, column=1, sticky='w', padx=10)

brentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
brentry.grid(row=4,column=2,pady=9,padx=10)
brentry.insert(0,0)


#macpuff
mplabel=Label(snacksframe, text='McPuff', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
mplabel.grid(row=5,column=0,sticky='w',padx=10)

mcpuff_price = get_price_from_csv('Mcpuff')
mpprice_label = Label(snacksframe, text=f' {mcpuff_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
mpprice_label.grid(row=5, column=1, sticky='w', padx=10)

mpentry=Entry(snacksframe,font=('times new roman',15,'bold'),width=3,bd=5)
mpentry.grid(row=5,column=2,pady=9,padx=10)
mpentry.insert(0,0)




#desserts------
dessertsframe=LabelFrame(productframe,text='Desserts', font=('times new roman',15,'bold'),fg='gold',
                    bd=8,relief=GROOVE,bg='#061c32')
dessertsframe.grid(row=0,column=2)


#cake
cakelabel=Label(dessertsframe, text='Cake', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
cakelabel.grid(row=0,column=0,sticky='w',padx=10)

cake_price = get_price_from_csv('Cake')
cakeprice_label = Label(dessertsframe, text=f' {cake_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
cakeprice_label.grid(row=0, column=1, sticky='w', padx=10)

cakeentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
cakeentry.grid(row=0,column=2,pady=9,padx=10)
cakeentry.insert(0,0)
is_numeric(cakeentry.get())
#pastry
pastrylabel=Label(dessertsframe, text='Pastry', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
pastrylabel.grid(row=1,column=0,sticky='w',padx=10)

pastry_price = get_price_from_csv('Pastry')
pastryprice_label = Label(dessertsframe, text=f' {pastry_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
pastryprice_label.grid(row=1, column=1, sticky='w', padx=10)

pastryentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
pastryentry.grid(row=1,column=2,pady=9,padx=10)
pastryentry.insert(0,0)

#pancakes
pancakelabel=Label(dessertsframe, text='Pancakes', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
pancakelabel.grid(row=2,column=0,sticky='w',padx=10)

pancake_price = get_price_from_csv('Pancakes')
pancakeprice_label = Label(dessertsframe, text=f' {pancake_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
pancakeprice_label.grid(row=2, column=1, sticky='w', padx=10)

pancakeentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
pancakeentry.grid(row=2,column=2,pady=9,padx=10)
pancakeentry.insert(0,0)

#strawberry truffle
trufflelabel=Label(dessertsframe, text='Truffle', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
trufflelabel.grid(row=3,column=0,sticky='w',padx=10)

st_price = get_price_from_csv('Strawberry Truffle')
stprice_label = Label(dessertsframe, text=f' {st_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
stprice_label.grid(row=3, column=1, sticky='w', padx=10)

truffleentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
truffleentry.grid(row=3,column=2,pady=9,padx=10)
truffleentry.insert(0,0)

#creamroll
crlabel=Label(dessertsframe, text='Cream Roll', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
crlabel.grid(row=4,column=0,sticky='w',padx=10)

cr_price = get_price_from_csv('Cream Roll')
crprice_label = Label(dessertsframe, text=f' {cr_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
crprice_label.grid(row=4, column=1, sticky='w', padx=10)

crentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
crentry.grid(row=4,column=2,pady=9,padx=10)
crentry.insert(0,0)

#cupcake
cclabel=Label(dessertsframe, text='Cupcake', font=('times new roman',15,'bold'),fg='white',
                     bg='#061c32')
cclabel.grid(row=5,column=0,sticky='w',padx=10)

cc_price = get_price_from_csv('Cupcake')
ccprice_label = Label(dessertsframe, text=f' {cc_price} Rs.', font=('times new roman', 15, 'bold'),
                      fg='white', bg='#061c32')
ccprice_label.grid(row=5, column=1, sticky='w', padx=10)

ccentry=Entry(dessertsframe,font=('times new roman',15,'bold'),width=2,bd=5)
ccentry.grid(row=5,column=2,pady=9,padx=10)
ccentry.insert(0,0)

#-----------BILL AREA------------------------
billframe=Frame(productframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

#billarea label------------
billarealabel=Label(billframe,text='BILL AREA', font=('times new roman',15,'bold'),bd=7
                         ,relief=GROOVE)
billarealabel.pack(fill=X)

#scroll bar---------------
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

#text area----------------
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

#bill menu---------------
billmenuframe=LabelFrame(root,text='BILL MENU', font=('times new roman',15,'bold'),fg='gold',
                    bd=8,relief=GROOVE,bg='#061c32')
billmenuframe.pack(fill=X)

bevpricelabel=Label(billmenuframe,text='BEVERAGE PRICE',font=('times new roman',15,'bold'),bg='#061c32',
                    fg='white')
bevpricelabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bevpriceentry=Entry(billmenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
bevpriceentry.grid(row=0,column=1,pady=9,padx=10)

snackspricelabel=Label(billmenuframe,text='SNACKS PRICE',font=('times new roman',15,'bold'),bg='#061c32',
                    fg='white')
snackspricelabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
snackspriceentry=Entry(billmenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
snackspriceentry.grid(row=1,column=1,pady=9,padx=10)

dessertspricelabel=Label(billmenuframe,text='DESSERTS PRICE',font=('times new roman',15,'bold'),bg='#061c32',
                    fg='white')
dessertspricelabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
dessertspriceentry=Entry(billmenuframe,font=('times new roman',15,'bold'),width=10,bd=5)
dessertspriceentry.grid(row=2,column=1,pady=9,padx=10)



#--------------button frame------------
buttonframe=Frame(billmenuframe,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=6,rowspan=3,padx=400)

#totalbutton---------
totalbutton=Button(buttonframe,text='TOTAL',font=('arial',16,'bold'),bg='#061c32',fg='white',bd=5,width=8,
                   pady=10,command=total)
totalbutton.grid(row=0,column=1,pady=20,padx=5)


#billbutton---------
billbutton=Button(buttonframe,text='BILL',font=('arial',16,'bold'),bg='#061c32',fg='white',bd=5,width=8,
                   pady=10,command=bill)
billbutton.grid(row=0,column=2,pady=20,padx=5)


#clearbutton---------
clearbutton=Button(buttonframe,text='CLEAR',font=('arial',16,'bold'),bg='#061c32',fg='white',bd=5,width=8,
                   pady=10,command=clear)
clearbutton.grid(row=0,column=4,pady=20,padx=5)


#exitbutton---------
exitbutton=Button(buttonframe,text='EXIT',font=('arial',16,'bold'),bg='#061c32',fg='white',bd=5,width=8,
                   pady=10,command=exit_program)
exitbutton.grid(row=0,column=5,pady=20,padx=5)

root.mainloop()


