#list comprehence
celsius = [10, 21]
farenheit = [cls * 9/5 + 32 for cls in celsius]

#practice
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [item1 for (item1, item2) in nested_lists]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
combined = list(zip(a, b))
sums = [item + item1 for (item, item1) in combined]

a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]

combined = list(zip(a, b))
quotients = [(item1 / item ) for (item, item1) in combined]


capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]
combined = list(zip(capitals, countries))
locations = [capital + ", " + country for (capital, country) in combined]

names = ["Jon", "Arya", "Ned"]
ages = [14, 9, 35]
users = ["Name: " + name + ", Age: " + str(age) for (name, age) in zip(names, ages) ]

a = [30, 42, 10]
b = [15, 16, 17]
greater_than = [itemA > itemB for (itemA, itemB) in zip(a, b)]
