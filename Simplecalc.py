x=float(input("Enter the first number="))
y=float(input("Enter the Second number="))
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
print("Select any operations\n" \
      "1. Addition\n" \
      "2. Subtraction\n" \
      "3. Multiplication\n" \
      "4. Division\n")
select=int(input("Select any operations 1, 2, 3, 4:"))
if select == 1 :
 print(x,"+",y,"=",add(x,y))
elif select == 2:
 print(x,"-",y,"=",sub(x,y))
elif select == 3:
 print(x,"*",y,"=",mul(x,y))
elif select == 4:
 print(x,"/",y,"=",div(x,y))
else:
 print("Invalid Input")
