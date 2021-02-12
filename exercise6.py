# GETTING A NAME
def getting_name():
    name = str(input("Name: "))
    return name

def name_lenght(name):
    tam = 0
    for i in range(len(name)):
        if name[i] != (""):
            tam += 1

    print(tam)
    
def main():
    name = getting_name()
    name_lenght(name)
main()