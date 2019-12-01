# Video 6 and 7 Code basics Hindi

#n1=input("Enter first number")
#n2=input("Enter Second number")
#print(type(n1))
#print(type(n2))
#print("hello world",float(n1)+float(n2))

Mithai=['hava','jalebi','gulab jamun','rosgulla','kheer']
#print(Mithai)
#print(type(Mithai))
#print(Mithai[1]) # we can use negative element
#print(Mithai[1:3])
#print(len(Mithai))
#print('samosa' in Mithai)
#print('samosa' not in Mithai)
#print(Mithai.append('laddu'))
#print(Mithai)
#print(Mithai.insert(4,'kulfi'))
#print(Mithai)
#tikha = ['Kachori','Sev']

#food = Mithai+tikha
#print(food)
#Mithai[2] = 'Peda'
#print(Mithai)
#Mithai[0:2] = ['Malai','Besan']
#print(Mithai)
#Mithai[3:4] = [4,5]
#print(Mithai)

jan = 2200
feb = 2350
mar = 260
apr = 2130
may = 2190

Mon = [2200,2350,2600,2130,2190]

Extra_Feb = feb - jan
#print("Total amount spend Extra in Feb \t",Extra_Feb)
#print('Total Expense in First Quarter is\t', jan+feb+mar)

'''print("Total amount spend Extra in Feb \t",Mon[1]-Mon[0])# Exercise from video 7
print("Total amount spend in 1st Quarter \t",Mon[0]+Mon[1]+Mon[2]) # Exercise from video 7
print("Did I spend Exactly $2000 in any month\t",2000 in [Mon]) # Exercise from video 7
Mon.append(1980) # Exercise from video 7
print(Mon) # Exercise from video 7
Mon[3]=Mon[3]-200 # Exercise from video 7
print("Correct Amount for the month of April",Mon) # Exercise from video 7
print(Mon) # Exercise from video 7
'''

heroes=['spider man','thor','hulk','iron man','captain america']
print(len(heroes))
heroes.append('black panther')
print(heroes)
heroes.remove('black panther')
heroes.insert(3,'black panther')
print(heroes)

heroes[1:3]=['doctor strange']
print(heroes)

heroes.sort()
print(heroes)
