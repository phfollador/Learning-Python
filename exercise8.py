# GETTING A NAME
def getting_name():
    name = input("Name: ")
    return name

# PRINTING IT REVERSE
def print_reverse(name):
    return name[::-1]
    
def main():
    name = getting_name()
    rev = print_reverse(name)
    print(rev)
main()