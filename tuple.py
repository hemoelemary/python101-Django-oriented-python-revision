#tuple vs list
# immutable vs mutable = not changeable vs changeable

#list
animals = ['cat','dog','zebra','a']
animals.sort() #change main list
print(animals)
#tuple
#not change accept count and index
#memory performance
foods = ('pizza','orange','apple','pasta',) # ,) at end means for sure it's a tuple
print(foods)

for food in foods:
    print('food is',food)

# at end tuples are restricted lists