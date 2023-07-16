import csv




with open("life-expectancy.csv") as data:

    data.readline()

    for line in data:

        line = line.strip()

        clean_line = line.split(",")




        entity = clean_line[0]

        code = clean_line[1]

        year = clean_line[2]

        life_expectancy = clean_line[3]

        

        life_expectancy = float(life_expectancy)

        print(life_expectancy)
