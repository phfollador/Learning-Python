import numpy as np
# GETTING NUMBERS
def getting_numbers():
    number = int(input("Number: "))
    return number

def print_all_numbers(number):
    l = []
    for i in range(1, number+1):
        l.append([i])

    print(l)
    print(np.prod(l))

def main():
    number = getting_numbers()
    print_all_numbers(number)
main()