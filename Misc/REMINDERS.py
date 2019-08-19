#Python reminders

# Collapse the list for output
''.join(list)

#Flatten list of lists
flat_list = [item for subitem in lists for item in subitem]

#Exammple for checking list for single digit (string)
def checker(string):
	print("Boom!" if "7" in str(string) else "there is no 7 in the list")
checker([2, 55, 60, 97, 86, 3, 4, 6, 6])

#Scan list for longest string and print max item
print(max(len(i) for i in string.split()))

#Dont forget min and max
max(x) for largest
min(x) for smallest

#Count occurrences of item in list
[a,b,c,d,e].count(item) 

#put anything in square brackets to search list index
a[0]
#reverse list of ints by converting to string and list reversing
str(num)[::-1]

#Strange list rotation
def rotate_left3(nums):
  a = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = a
  return nums -> [1,2,3] = [2,3,1]

#Evaluator positioning
if someting:
	return (item 1 >= 10)
else:
	return (item > 1 and item <= 5)

#One line conditionals
	#get item index from lst, not there, return -1
return lst.index(item) if item in lst else -1

#Use F strings
x = "hello"
w = "world"
print(f"{x} {w}")

#List comprehensions
	#example CW solution used to reverse all words >= 5 letters and print out the modified sentence
	[word[::-1] if len(word) >= 5 else word for word in words]
	#Example CW solution to create a dictionary of letters and their frequency of occurrence in a string
	{i : message.count(i) for i in set(message)}
	#Example edabit solution to list all indexes of a specified value
	def get_indicies(lst, el):
	[i for i in range(len(lst)) if lst[i] == el]
	#Only return the integers in a list
	[x for x in l if type(x) == int]
	#Flatten list of lists
	flat_list = [item for subitem in lists for item in subitem]

#Collapse multiple inputs into one
	#from this
	def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
	#to this
	def predict_age(*ages)

#Remove char
def remove_exclamation_marks(s):
    return s.replace('!', '')

#remove duplicate words
def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key = s.index))

#Quick Lambda implementation on multiple args - with f"string"
def newvibe(a,b,c):
	var1 = lambda x: (x * 5)
	print(f"This is a: {var1(a)}, This is b: {var1(b)}, This is c: {var1(c)}")
