# Create a list
wizards = []
death_eater = ["Lucas","Barty","Bellatrix"]


#Example 1 : add a couple of wizards
wizards.insert(0,"Harry")  #----- insert(0,Harry) will put Harry in the first column
wizards.insert(0,"Hermione") #----- insert(0,Hermione) will push Harry down to the next row and put Hermione in the first column

#wizards.append("Harry") #-----work like above, insert(0,Harry) will put Harry in the first column

print(wizards)

#Example 2 : Add more to the wizards list
wizards.extend(death_eater) #---the 'extend' property is what adds multipe to the list 

print(wizards)

#Example 3 : Remove an Item
wizards.remove("Barty")

print(wizards)

#Example 4: using 'pop' to remove Item from a list. Though it put the item in a new row
bella = wizards.pop(-1)
print(bella)

#Example 5: Clearing everything in the list. Result will show [] meaning blank
wizards.clear()

print(wizards)

