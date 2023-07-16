import math 

farenheit_temp = float(input("What is the temperature in Farenheit?"))
celcius_temp = (farenheit_temp - 32) * 5 / 9

print(f"The temperature in Celsius is {celcius_temp:.1f} degrees.")

input("Press ENTER to EXIT")
