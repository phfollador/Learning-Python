# READ A NAME, PHONE AND ADDRESS. PRINT THEM

# GETTING A NAME
def getting_name():
    name = str(input("Name: "))
    return name

# GETTING A PHONE
def getting_phone():
    phone = int(input("Pone: "))
    return phone

# GETTING ADDRESS
def getting_address():
    address = str(input("Address: "))
    return address 

# PRINTING
def print_data(name, phone, address):
    print(name, phone, address)

# MAIN FUNCTION
def main():
    name = getting_name()
    phone = getting_phone()
    address = getting_address()
    print_data(name, phone, address)
main()