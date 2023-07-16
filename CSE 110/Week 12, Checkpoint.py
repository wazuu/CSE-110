people = [
    "Joe 20",
    "Jacob 45",
    "Claire 24",
    "Hulk 76",
    "Mike 37",
    "Mellissa 34",
    "Melva 55",
    "Pete 63"
]
youngest_age = 9999
youngest_name = ""
for person_line in people:
    parts = person_line.split()
    name = parts[0]
    age = int(parts[1])
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")