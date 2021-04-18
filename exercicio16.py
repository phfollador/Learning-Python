def numero():
    n = int(input("Entre com um valor inteiro de N: "))
    return n

def matriz(n):
    val = 0
    tot = n+1

    for col in range(1, tot):
        for lin in range(1, tot):
            if(lin < tot):
                val += n
                print(val, end="  ")
            if(lin == tot-1):
                print("\n")

        n -= 1
        val = 0

def main():
    n = numero()
    matriz(n)
main()