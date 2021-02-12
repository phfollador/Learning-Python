# GETTING SALARY
def getting_salary():
    salary = float(input("Salary: "))

    return salary

# GETTING RENDER
def getting_render():
    render = float(input("Render: "))

    return render

# LOAN CALC
def loan_calc(salary, render):
    if render > salary*0.2:
        print("LOAN CANNOT BE GRANTED")
    else:
        print("LOAN CAN BE GRANTED")

def main():
    render = getting_render()
    salary = getting_salary()
    loan_calc(salary, render)
main()