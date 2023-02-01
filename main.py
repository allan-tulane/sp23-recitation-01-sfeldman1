"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
#import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
    if right >= left:
      mid = (right + left)//2
      if key == mylist[mid]:
         return mid
      elif key > mylist[mid]:
         return _binary_search(mylist, key, mid+1, right)
      else:
         return _binary_search(mylist, key, left, mid-1)
    else:
      return -1

	### TODO

	###

def test_binary_search():
	assert binary_search([1,2,3,4,5], 5) == 4
	assert binary_search([1,2,3,4,5], 1) == 0
	assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3,4,5,6,7], 2) == 1
  assert binary_search([4,5,6,7,8,9,10,11,12], 5) == 1
	### TODO: add two more tests here.

	###


def time_search(search_fn, mylist, key):
	"""
	Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
	"""
  start_time = time.time()
  search_fn(mylist, key)
  end_time = time.time()
  t = end_time - start_time
  mill = t * 1000
  return mill
	### TODO

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
	
  results_list = []
  
  for i in sizes:
    
     mylist = list(range(int(i)))
     time_linear = time_search(linear_search, mylist, -1)
     time_binary = time_search(binary_search, mylist, -1)
     curr_tuple = (i, time_linear, time_binary)
     results_list.append(curr_tuple)

  
  return results_list
	### TODO

	###

def print_results(results):
	""" done """
	##print(tabulate.tabulate(results,
						##	headers=['n', 'linear', 'binary'],
							##floatfmt=".3f",
						##	tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
