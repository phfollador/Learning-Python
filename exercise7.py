# GETTING A NAME
def getting_name():
    name = str(input("Name: "))
    return name

# GETTING NAME LENGHT
def name_lenght(name):
    tam = 0
    for i in range(len(name)):
        if name[i] != (""):
            tam += 1

    return tam

# PRINTING NAME TIMES
def printing_name_times(tam, name):
    for i in range(0, tam):
        print(name)
    
def main():
    name = getting_name()
    lenght = name_lenght(name)
    printing_name_times(lenght, name)
main()