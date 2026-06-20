employee_name = input("Enter Employee's name : ")
basic_salary = int(input("Enter your salary in numbers only : "))
experience = float(input("Mention your experience in years and months (for eg. write 2.5 for 2 and half years) : "))


if experience>=5 :
              bonus_amount = basic_salary*0.20 
              total_salary = bonus_amount + basic_salary
            
elif experience>=2 :
              bonus_amount = basic_salary*0.1 
              total_salary = bonus_amount + basic_salary
              
else :
              total_salary = basic_salary
              
tax = total_salary * 0.05
net_salary = total_salary - tax          

print("Employee's name : ",employee_name)
print("Basic Salary : ", basic_salary)
print("Bonus amount : ",bonus_amount)
print("Amount of tax deducted : ", tax)
print("Final Salary : ", net_salary)