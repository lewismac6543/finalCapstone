#========The beginning of the class==========

# Defining the shoe class
class shoe:
    
    # Defining the independent variables of each line of the inventory
    def __init__(self, country, code, product, cost, quantity):
        pass
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Defining the get_cost method
    def get_cost(self):
        pass
        return self.cost

    # Defining the get_quantity method
    def get_quantity(self):
        pass
        return self.quantity

    # Defining the format of the string
    def __str__(self):
        pass
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"


#=============Shoe list===========

# The list will be used to store a list of objects of shoes.
shoe_list = []

#==========Functions outside the class==============

# Defining a function to read from the inventory.txt file and store the data
def read_shoes_data():
    pass

    # Creating an exception for when the file doesn't exist that stops the program from crashing
    try:
        with open("inventory.txt", "r") as file:
            
            # Skip the first line of the file
            next(file)

            # Add the data from the text file to the shoe_list array
            for line in file:
                data = line.strip().split(",")
                shoe_list.append(shoe(*data))

    except Exception as e:

        # Prints the specific error to the user
        print(f"Error reading file: {e}")

# Defining a function to add a new shoe to the inventory text file
def capture_shoes():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()

    # Requesting the user for the information of the shoe to add to the text file
    try:
        
        # Requesting the user for the information of the shoe to add to the text file
        country = input("Enter the country of origin:\t")
        code = input("Enter the product code:\t")
        product = input("Enter the product name:\t")
        cost = int(input("Enter the cost price:\t"))
        qty = int(input("Enter the quantity:\t"))

    # An exception error for when the user tries to enter a non integer for either cost or quantity
    except ValueError:
        print("Invalid input. Integers only allowed for cost and quantity.")
        return

    # Appending this to the shoe_list array
    shoe_list.append(shoe(country, code, product, cost, qty))

    # Writing over the original text file with the header and the appended array
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")
        for shoes in shoe_list:
            file.write(str(shoes) + "\n")

# Defining a function to view all the shoes in the inventory
def view_all():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()

    # Printing every item in shoe list
    for shoe in shoe_list:
        print(shoe)

def re_stock():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()

    # Setting blank variables to use in the for loop
    min_qty = 1000000000000
    min_qty_shoe = None

    # Repeat for every item in the inventory. If the shoe quantity is less than the min quantity then make the shoe quantity the min quantity, and record the shoe with the min quantity
    for shoe in shoe_list:
        if int(shoe.quantity) < int(min_qty):
            min_qty = shoe.quantity
            min_qty_shoe = shoe
    
    # Printing out the information about the shoe with the lowest quantity to the user
    if min_qty_shoe:
        print(f"The product with the smallest quantity is {min_qty_shoe.product} with {min_qty} units")
    
    # Ask the user if they would like to add more stock to this shoe
    choice = input("Do you want to add more pairs of this shoe ('yes' or 'no')?\t").lower()

    # If the user has selected yes, ask them how many shoes they wish to add and add this to the shoes quantity. Then let the user know what the new total stock for the shoe is
    if choice == 'yes':
        add_qty = int(input("Enter the quantity of shoes to add: "))
        min_qty_shoe.quantity = int(min_qty_shoe.quantity) + add_qty
        print(f"{add_qty} pairs of {min_qty_shoe.product} ({min_qty_shoe.code}) have been added. The total is now: {min_qty_shoe.quantity}")
        
        # Setting up an exception rule to stop the program from crashing, primarily for when the file doesn't exist
        try:

            # Opening the file to read every individual line and store it as a variable to use
            with open("inventory.txt", "r") as file:
                lines = file.readlines()
            
            # Opening the file to write over 
            with open("inventory.txt", "w") as file:
                
                # Repeat for every line taken from the inventory.txt file
                for line in lines:

                    # If the identified shoe with the minimum quantity is found in the line then replace the existing quantity with the new quantity and write the line back to the file
                    if min_qty_shoe.code in line:
                        data = line.strip().split(",")
                        data[-1] = str(min_qty_shoe.quantity)
                        file.write(",".join(data) + "\n")
                    
                    # If the identified shoe with the minimum quantity is not found in the line then just write the existing line back to the file
                    else:
                        file.write(line)

        except Exception as e:
            print(f"Error: {e}")
    
    # If the user has selected no return the user to the main menu
    else:
        return
 
# Defining a function to search for a specific shoe in the inventory
def seach_shoe():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()

    # Requesting the user to input the code of the shoe they wish to look up
    code = input('Enter shoe code:\t')

    # For every shoe in the inventory search to see if the code inputted matches. If the code matches output the shoes information to the user. If the code does not match let the user know the shoe has not been found.
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print('Shoe not found.')

# Defining a variable to find the value of each type of shoe in the inventory
def value_per_item():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()
    
    # Repeat for every shoe in the inventory, multiply the value of the shoe against it's quantity and output this to the user
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f'Product: {shoe.product}. Code: {shoe.code} has a total value of {value}.')

# Defining a variable to find the shoe that has the highest quantity in stock
def highest_qty():
    pass
    
    # Calling the read_shoes_data to make sure the shoe_list array is updated
    read_shoes_data()

    # Setting blank variables to use in the for loop
    max_qty = 0
    max_qty_shoe = None

    # Repeat for every item in the inventory. If the shoe quantity is greater than the max quantity then make the shoe quantity the max quantity, and record the shoe with the max quantity
    for shoe in shoe_list:
        if int(shoe.quantity) > int(max_qty):
            max_qty = shoe.quantity
            max_qty_shoe = shoe
    
    # Printing out the information about the shoe with the highest quantity to the user
    if max_qty_shoe:
        print(f"The product with the highest quantity is {max_qty_shoe.product} with {max_qty} units")

    # Printing that the shoe is now available for sale
    print(f"Product: {max_qty_shoe.product}, is now for sale")

#==========Main Menu=============

# Defining the main function which includes the main menu of the program
def main():
    while True:
        
        # Outputting the menu to the user
        print("Welcome to the Shoe Inventory System! Please choose an option:")
        print("1. Read shoes data from inventory.txt")
        print("2. Capture a new shoe")
        print("3. View all shoes")
        print("4. Re-stock a shoe")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Determine the product with the highest quantity")
        print("8. Exit")

        # Requesting the user to select an option
        option = input("Enter your choice:\t")

        # Calling the corresponding function of the option the user selected
        if option == "1":
            read_shoes_data()
        elif option == "2":
            capture_shoes()
        elif option == "3":
            view_all()
        elif option == "4":
            re_stock()
        elif option == "5":
            seach_shoe()
        elif option == "6":
            value_per_item()
        elif option == "7":
            highest_qty()
        elif option == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Calling the main function
main()
