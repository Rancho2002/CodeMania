#import the module
import bisect

#given sorted list of numbers
nums = [1,3,5,7,10,25,49,55]

#given element to be inserted into the list
ele = 25

#get index where to insert the element
idx = bisect.bisect_left(nums, ele)

#!to add the new element use bisect.insort_left(nums, ele)

#print the index
print(f"Insert element {ele} at index {idx} in nums list to maintain sorted order.")