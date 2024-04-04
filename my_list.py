#create an empty list 
my_list = []

#append elements 10,20,30,40
elements =  [10,20,30,40]

for element in elements:
	my_list.append(element)

#insert the value 15 at the second position
my_list[1] = 15
#extend with elements 50,60,70
extend_elements = [50,60,70]

for extend_element in extend_elements:
	my_list.append(extend_element)

#remove the last element

my_list.remove(my_list[6])

#sort the list ascending order {already in ascending order}

my_list = sorted(my_list)

#Find and print the index of the value 30

	
index_0f_30 = my_list.index(30)

print("The index of 30 is:",index_0f_30)


