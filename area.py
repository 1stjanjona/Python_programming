str_length = input("Please type Length: \n")
str_width = input("Please type width: \n")
str_price = input("How much for 1 meter? : \n")

length = float(str_length)
width = float(str_width)
price = float(str_price)

area = length * width
total_price = price * area

str_area = str(area)
str_total_price = str(total_price)
print("The total area is: " + str_area)
print("The total price is: Dz" + str_total_price)
