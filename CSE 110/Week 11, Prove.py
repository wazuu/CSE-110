import statistics
with open("life-expectancy.csv") as life:
    next(life)
    output = []
    for line in life:
        clean_line = line.strip()
        split_line = clean_line.split(",")
        entity = split_line[0]
        code = split_line[1]
        year = split_line[2]
        life_expectancy = float(split_line[3])
        output.append([entity, code, year, life_expectancy])
min_life = min(output, key=lambda x: x[3])
max_life = max(output, key=lambda x: x[3])
date = input("Please enter a date: ")
print(f"The lowest life expectancy is {min_life[3]} in {min_life[0]},")
print(f"The longest life expectancy is {max_life[3]} in {max_life[0]},")
print(f"The countries with the lowest and hightest life expectancy is  sum{min_life} , sum{max_life}")
print(f"The average life expectancy for {date} is {life_expectancy} in {entity}")