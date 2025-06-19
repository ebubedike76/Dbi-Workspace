# Friuts list
fruits = ["Orange", "Apple", "bannan", "pinapple", "mango"]

# Access elements in the lists
#print(friuts[0])

#print out friuts that start with a specific letter 
for fruit in fruits:
  if(fruit[0] == 'a'):
    print(fruit)
    fruits.remove(fruit)
    fruits.append("Jed ate this fruit")


  print("---------------")

  # for loop with enumerate
  for index, friut in enumerate(fruits, start=0):
    print(fruit)

  print("---------------")


  # for loop with range
  for i in range(len(fruits)):
    print(fruits[i])

  print(fruits)

  # List Comprehension
  numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

  double = [x * 2 for x in numbers]

  print(double)  
