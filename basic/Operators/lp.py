result = 0
while True:
        number = int(input("Enter a number : "))
        if number != 0 :
              print("the entered number is : ", number)
        else:
              for i in number:
                      result += i
                      print('The total numbers entered are : ',i)
              break

''' Keep asking the user for numbers.

When the user enters:

0

stop the loop.

At the end display:

Total Numbers Entered'''