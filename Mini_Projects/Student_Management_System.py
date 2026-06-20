name = input("Enter your name : ")
marks_1 = int(input("Enter your marks in Subject 1 : "))
marks_2 = int(input("Enter your marks in Subject 2 : "))
marks_3 = int(input("Enter your marks in Subject 3 : "))

total = marks_1+marks_2+marks_3

percentage = total/300*100

if marks_1<35 or marks_2<35 or marks_3 < 35:
        Grade = 'F'
        result = 'Fail'
        print(f"Result : {result}")
elif percentage>=90:
        Grade = 'A'
        result = 'pass'
        print(f"{Grade}, {result} ")
elif percentage>=75:
        Grade = 'B'
        result = 'pass'
        print(f"{Grade}, {result} ")
elif percentage>=60:
        Grade = 'C'
        result = 'pass'
        print(f"{Grade}, {result} ")

else:
        Grade = 'F'
        result = 'Fail'
        print("Fail")

print("Name = ", name)
print("Total = ", total)
print("Percentage = ", percentage)
print(f"Grade : {Grade}")
print(f"Result': {result}")