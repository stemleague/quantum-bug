############### Beginner Level Challenges ###############
def test1():
	# given lists
  a_list = ["apple", "banana", "peaches", "oranges"]
  b_list = ["avocado", "carrot", "strawberry"]

	# insert all items from b_list to a_list in alphabetical order

  
  # create a new c_list


  # add all items from a_list that start with a vowel into c_list


# Uncomment the next line to test if your code works
# test1()



def test2():
  print("Welcome to Baskin Robbins! Please scan your items below.")
  apply_discount = True # You can change this around to test your code

  # Scott will input items into the register
  item1 = input("item 1 name: ")
  item1_cost = input("item 1 cost: ")

  item2 = input("item 2 name: ")
  item2_cost = input("item 2 cost: ")

  total = 0
  # apply discount of 80% off if apply_discount is true
  if not apply_discount:
    total = (item2_cost) + 0.8

  print("total", total)
  
# Question: Will your solution work for all item costs (floats, integers)?

# Uncomment the next line to test if your code works
# test2()



############### Intermediate Level Challenges ###############
def test3():
  my_list = [1, 4, 5, 2, 3, 9, 2, 3]

  # remove duplicate values from my_list


  # print out my_list after sorting values


# Question: Can you solve test3() using Python sets? How about with lists?

# Uncomment the next line to test if your code works
# test3()



def test4():
  words = ["t", "real", "B", "L", "is", "not", "v", "took", "stole", "never", "stones", "were", "infinity", "A", "tV", "MOBiuS", "T", "he", "ehT", "JET5", "3skis", "pRUne", "ER"]

  # You can uncomment the next two lines to see the index of each item in your list, which is helpful to solve this challenge.
  # for i in range(len(words)):
  #   print(words[i], i)

  # Print out “The TVA is not real” using list indexing methods

  # Print out “MOBIUS the jet skier”

# Uncomment the next line to test if your code works
# test4()



############### Advanced Level Challenge ###############
def test5():
  my_str = "niagrab ot emoc ev’i ummamrod"
  # Write code to reverse my_str

# Question: Can you do this in a one line solution using string indices?

# Uncomment the next line to test if your code works
# test5()
