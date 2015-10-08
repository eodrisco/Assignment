import numpy as np
import cmath

# still with having trouble with sqlite3 module, in putting db into numpy multiarray forma.
# using np.genfromtxt until I figure this out
# Get the file renew.txt.

X = np.genfromtxt("renew.txt")
#print X.shape
#print X

sum_weight1 = 0
sum_weight2 = 0
sum_weight3 = 0
sum_weight4 = 0
sum_weight5 = 0
sum_weight6 = 0
sum_weight7 = 0
sum_weight8 = 0
sum_weight9 = 0
sum_weight10 = 0

i  = 0
while i < 10:
    # distance to location1 
    # distance to loc1 is distance from loc1 to each other location multiplied by production of that plant
    distance1 = cmath.sqrt((X[i,0]-X[0,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1]))
    print distance1  
    # weighting each prodution facility is tonnage divide by distance
    # distance to current location is zero. If loop to work aroung this.
    if distance1 == 0:
         weight1 = X[i,2]
         print weight1
    else: 
         weight1 = X[i,2]/cmath.sqrt((X[i,0]-X[0,0])*(X[i,0]-X[0,0])+(X[i,1]-X[0,1])*(X[i,1]-X[0,1]))
         print weight1
    #sum weight of each location
    sum_weight1 = weight1 + sum_weight1
    
    i = i + 1
    
    print sum_weight1
    
    
    
    
    