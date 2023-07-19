from os import *
from sys import *
from collections import *
from math import *

def corpFlightBookings(bookings, n):
	# Write your code here.
	row=len(bookings)
	col=n

	ans=[[0 for _ in range(col)] for _ in range(row)]

	for i in range(row):
		ind=bookings[i][0] -1
		colInd=bookings[i][1]
		for j in range(ind,colInd):
			ans[i][j]= bookings[i][2]


	val=[]

	for i in range(col):
		s=0
		for j in range(row):
			s+=ans[j][i]
		val.append(s)

	return val


corpFlightBookings([[1,2,3],[2,3,2],[1,3,1],[3,4,2]],4)