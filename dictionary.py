# Write a program that will "glue" the two dictionaries (d1 and d2) together and create a new one (d3).

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    d3.update(item)
 
print(d3)
 
