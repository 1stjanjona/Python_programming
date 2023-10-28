#!/usr/bin/env python3
country = input("Choose a country where to deliver your order: (Algeria), (Egypt), or (Tunisia)\n")
area = country.capitalize()
if area == "Algeria" or area == "Egypt" or area == "Tunisia":
    print(f"We deliver to {area}, please provide us with more details to receive your order.")
else:
    print(f"We don't deliver to {area}, please check the nearest country to you on our list.")
