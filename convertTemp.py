fahr=float(input("Enter temperature in Fahrenheit:"))
celsius = (fahr - 32) * 5/9
kelvin=celsius+273.15
print(f"{fahr} in Fahrenheit is equal to {round(celsius, 2)} in Celsius and {round(kelvin, 2)} in Kelvin")