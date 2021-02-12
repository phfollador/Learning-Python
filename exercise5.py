# GET NAME, SEX AND AGE. IF SEX IS FEMALE AND AGE LESS THAN 25, PRINT NAME AND "ACCEPT", IF NOT, "NOT ACCEPT"

# GETTING A NAME
def getting_name():
    name = str(input("Name: "))
    return name

# GETTING AGE
def getting_age():
    age = int(input("Age: "))
    return age

# GETTING SEX
def getting_sex():
    sex = str(input("Sex: "))
    return sex 

# CHECKING DATES
def check(name, age, sex):
    if sex == 'f' or sex == 'F' or sex == 'FEMALE' or sex == 'Female' or sex == 'female':
        if age < 25:
            print("ACCPET")
        else:
            print(end="")
    else:
        print("NOT ACCPET")

def main():
    name = getting_name()
    age = getting_age()
    sex = getting_sex()
    check(name, age, sex)
main()