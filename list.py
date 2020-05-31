# How to create a list of lists using zip
# How to add elements to a list using either .append() or +
# How to use range to create lists of integers


rangeOneList = range(startIndex, endIndex, skipDifference)
rangeTwoList = range(startIndex, endIndex)
list1 = range(5, 15, 3)
list2 = range(0, 40, 5)

first_names = ['Soli', 'Albert']
last_names = ['Sharipov', 'Smith']

full_names = zip(first_names, last_names) #(('Soli', 'Sharipov'), ('Albert', 'Smith'))

#list slicing [start:end]
name = first_names[0:1] #soli

# counting elements in list
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)

votes.sort() #sorts a list
sorted_votes = sorted(votes)
