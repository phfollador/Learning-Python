import numpy as np
# SHOW ALL NUMBERS DIVISIBLE BY 4 BLOW 200

# CREATE A LIST
l = np.linspace(1, 200, num=200)

# NUMBERS DIVISIBLE BY 4
def divisible():
    for i in range(len(l)):
        if l[i] <= 200 and l[i]%4 == 0:
            print(l[i], end=", ")

def main():
    divisible()
main()