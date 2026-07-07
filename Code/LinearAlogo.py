import random 

number_trials = 1000
worst_query = 0
list_items = range(50)

for i in range(number_trials):

  marked_item = random.choice(list_items)
  number_queries = 0
  for item in list_items:

      number_queries = number_queries + 1

      if item == marked_item:
          print(str(marked_item) + " has been found in " + str(number_queries) + " queries.")
          break

  worst_query = max(worst_query, number_queries)

print("Worst number of queries: " + str(worst_query))