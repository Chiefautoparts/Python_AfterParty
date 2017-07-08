myThing = [1,2,3,4,5]
for x in range(2, len(myThing) - 1):
	myThing[x] = myThing[x+1]
print myThing