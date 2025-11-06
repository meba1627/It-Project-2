x=int(input("Enter the temperature you want to convert into Fahrenheit:"))
y=input("Enter the first letter of to what unit you want to chnage the unit: ")
if y=="c":
    print(x*1.8+32,"c")
elif y=="k":
    print(x*1.8+32+273.15,"k")
else: print(y,"f")
    