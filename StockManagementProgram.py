#Final project by Hosam Ahmed
#Produts chosen: computers
#creating a stockList
barcode = [12345, 6789, 5566]
brand = ["Apple", "Dell", "Asus"]
category = ["Business-use", "Home-use", "Gaming"]
price = [400, 600, 800]
quantity = [10, 20, 50]

#setting up addProduct function
def addProduct():
    code=int(input("Please enter computer code: "))
#loop if product already exists
    while code in barcode:
        print("This product already exists - Please try again")
        addProduct()
#if new product code keyed by user, continue and update lists
    while code not in barcode:
        barcode.append(code)
        computer_brand=input("Please enter computer brand: ")
        brand.append(computer_brand)
        computer_category=input("Please enter computer category: ")
        category.append(computer_category)
        cost=float(input("Please enter computer price: "))
        price.append(cost)
        amount=int(input("Please enter quantity: "))
#setting quantity parameters as per project instructions  
        while (10>amount or amount>50):
            print("Incorrect - Quantity must be between 10 - 50, Please try again.")
            amount=int(input("Please enter quantity: "))
        quantity.append(amount)    
#option for user to add another product  
        cont=input("Would you like to add another product - Enter Y/N: ")
        if cont == 'Y' or cont == 'y' or cont == 'Yes' or cont == 'YES' or cont == 'yes':
            addProduct()
        else:
            print("-------------------------------------")
            print("\n**You are now back at the main menu.**\n")
        break        
#checking if product is already in stockList
def checkProduct(code):
    if code in barcode:
        return True
    else:
        return False
#Searching for a product
def searchProduct(code):
    if (checkProduct(code))==(True):
        print("Computer code is: ",barcode[barcode.index(code)])
        print("Computer brand is: ",brand[barcode.index(code)])
        print("Computer category is: ",category[barcode.index(code)])
        print("Computer price is: ",price[barcode.index(code)])
        print("Quantity is: ",quantity[barcode.index(code)],"\n")
    else:
        print("No product found!\n")
        new_code=int(input("Please enter another code: "))
        print("")
        searchProduct(new_code)
#Updating a product
def updateProduct(code):
    #asking user if they want to update if code already exists
    if (checkProduct(code))==(True):
        searchProduct(code)
        update=input("Do you want to update brand? - Please enter Yes or No: ")
        if update== 'Y' or update== 'y' or update=='yes' or update=='YES' or update=='Yes':
            computer_brand=input("Enter new brand: ")
            brand[barcode.index(code)] = computer_brand
            
        update=input("Do you want to update category? - Please enter Yes or No: ")
        if update== 'Y' or update== 'y' or update=='yes' or update=='YES' or update=='Yes':
            computer_cat=input("Enter new category: ")
            category[barcode.index(code)] = computer_cat      
        
        update=input("Do you want to update price? - Please enter Yes or No: ")
        if update== 'Y' or update== 'y' or update=='yes' or update=='YES' or update=='Yes':
            computer_price=float(input("Enter new price: "))
            price[barcode.index(code)] = computer_price        
        
        update=input("Do you want to update quantity? - Please enter Yes or No: ")
        if update== 'Y' or update== 'y' or update=='yes' or update=='YES' or update=='Yes':
            computer_quantity=int(input("Enter new quantity: "))
            while (computer_quantity>50 or computer_quantity<10):
                print("Incorrect - Quantity must be between 10 - 50, Please try again.")
                computer_quantity=int(input("Enter new quantity: "))
            quantity[barcode.index(code)] = computer_quantity
        print("")
        searchProduct(code)
    else:
        new_code=int(input("Code does not exist - Please enter another: "))
        print("")
        updateProduct(new_code)
    
#buying a product
def buyProduct(code,order):
    if checkProduct(code) == False:
        print("The code you enetered does not exist")
        code=int(input("Please enter a different code: "))
        order=int(input("Please enter quantity of the product: "))
        buyProduct(code,order)
    else:
        searchProduct(code)
#if user puts an amount more than amount in stock
        if order>quantity[barcode.index(code)] and quantity[barcode.index(code)] !=0:
            print(">> There are only", quantity[barcode.index(code)], "in stock for brand", brand[barcode.index(code)])
            again=(input("Do you want to enter new quantity, Enter Yes or No: "))
            if again=='Yes' or again=='y' or again=='YES' or again=='yes':
                order=int(input("Please enter quantity you want to buy: "))
                buyProduct(code,order)                    
        else:
#formula for calculating total cost            
            tax=order*price[barcode.index(code)]*0.15
            tax_total=(order*price[barcode.index(code)])+(tax)
            total0=(order*price[barcode.index(code)])+(tax)
            total1=(tax_total)-(tax_total*0.10)
            total2=(tax_total)-(tax_total*0.20)
            total3=(tax_total)-(tax_total*0.30)
#setting up cost based on quantity             
            if order<10 and quantity[barcode.index(code)] !=0:
                print("\nNo discount")
                print(">> Total price to pay (inc. GST)= $", total0)
                print('')
                print("-------------------------------------")
            elif (order==10 or 10<order<20) and quantity[barcode.index(code)] !=0:
                print("\n>> 10% discount applies")
                print(">> Total price to pay(inc. GST)= $", total1)
                print('')
                print("-------------------------------------")
            elif 20<=order<=30 and quantity[barcode.index(code)] !=0:
                print("\n>> 20% discount applies")
                print(">> Total price to pay(inc. GST)= $", total2)
                print('')
                print("-------------------------------------")
            elif order>30 and quantity[barcode.index(code)] !=0:
                print("\n>> 30% discount applies")
                print(">> Total price to pay(inc. GST)= $", total3)
                print('')
                print("-------------------------------------")
            else:
                print("------------------------------------------------")
                print("Sorry - This product is currently out of stock!")
                print("------------------------------------------------")
#stocklist updated after user buys product               
            quantity[barcode.index(code)] -= order
            if (quantity[barcode.index(code)] < 0):
                quantity[barcode.index(code)] = 0
        
#Main Program
selection = 1
while selection > 0:
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product")
    print("4. Buy Product")
    print("5. Exit\n")
        
    selection=int(input("Please select an option from the top menu (1-5): "))
    
    if selection == 1:
        print("\nYou have selected to Add a Product.")
        print("-------------------------------------")
        addProduct()
    elif selection == 2:
        print("\nYou have selected to Search Product.")
        print("-------------------------------------")
        code=int(input("Please enter computer code: "))
        print("")
        searchProduct(code)
        print("**You are now back at the main menu.**")
        print("-------------------------------------")
    elif selection == 3:
        print("\nYou have selected to Update Product.")
        print("-------------------------------------")
        code=int(input("Enter computer code: "))
        print("")
        updateProduct(code)
        print("**You are now back at the main menu.**")
        print("-------------------------------------")
    elif selection == 4:
        code=int(input("Please enter the code of the computer you want to buy: "))
        order=int(input("Please enter quantity you want to buy: "))
        print("")
        buyProduct(code,order)
        print("")
        print("**You are now back at the main menu.**")
        print("-------------------------------------")
    elif selection == 5:
        print("You have selected to Exit.")
        input("Press the ENTER key to continue.")
        selection=0
        exit
    else:
        print("\n**Incorrect choice - please choose from the displayed options**\n".upper())
        