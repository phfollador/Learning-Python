'''
CREATE AN ALGORITHM TATH READS THE LOWER AND UPPER LIMITS OF A RANGE 
AND PRINT ALL EVEN NUMBERS IN THE OPEN RANGE AND ITS SUMMATION. SUPPOSE
THE DATA ENTERED IS FOR A RANGE GROWING
'''

# GETTING LOWER LIMIT
def getting_lower():
    lower_limit = int(input("Lower: "))
    return lower_limit

# GETTING UPPER LIMIT
def getting_upper():
    upper_limit = int(input("Upper: "))
    return upper_limit

# RANGE SUMMATION
def range_sum(lower_limit, upper_limit):
    limit_sum = 0
    while lower_limit <= upper_limit:
        if lower_limit%2 == 0:
            print(lower_limit, end=", ")
            limit_sum += lower_limit
            lower_limit += 1
        else:
            lower_limit += 1

    print("SOMA: ", limit_sum)

def main():
    low = getting_lower()
    upe = getting_upper()
    range_sum(low, upe)
main()