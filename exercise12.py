'''
WRITE A PROGRAM THAT RECEIVES SEVERAL INTEGERS INT THE KEYBOARD AND AT THE END,
PRINT THE AVERAGE OF THE MULTIPLE NUMBERS OF 3. TO EXIT, PRESS 0.
'''

# GETTING INTEGERS
def getting_integers():
    opt = 1
    l = []
    summ = 0
    while opt != 0:
        number = int(input("Number: "))
        
        if number == 0:
            opt = 0
            for i in range(len(l)):
                summ = summ + l[i]

        else:
            l.append(number)
        
    print((summ)/len(l) * 3)            
    
def main():
    getting_integers()

main()