print("Lets determine the wind chill!")

def windspeed_calculation():
    for x in range (0, 60, 5):
        x += 5
        if f_c == "C":
            temperature_new = (temperature * 9/5) + 32
            wind_chill = 35.74 + (0.6215 * temperature_new) - 35.75 * (x**0.16) + (0.4275 * temperature_new * (x**0.16))
            print(f"At temperature {temperature_new}F, wind speed at {x}mph. The wind chill is: {wind_chill:.2f}F")
        elif f_c == "F":
            wind_chill = 35.74 + (0.6215 * temperature) - (33.75 * (x**0.16)) + (0.4275 * temperature * (x**0.16))
            print(f"At temperature {temperature}F, and wind speed at {x}MPH. The wind chill is: {wind_chill:.2f}F.")
        else: 
            print("That is not a valid answer")

temperature = float(input("What is the temperature?"))
f_c = input("Indicate either Fahrenheit or Celcius (F/C):").upper()
print()
windspeed_calculation()
