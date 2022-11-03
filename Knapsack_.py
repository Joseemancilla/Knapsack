

#####  Knapsack  #####
#### Jose Mancilla ####
### Independet Study ####


import sys
import numpy as np
import numpy



#Funtion read file
def readFile(file):
    fileObject = open("ks_82_0", "r")
    data = fileObject.read()
    print(data)


#This has the capacity of knapSack (W)
def capacity(file):
    with open('ks_82_0', "r") as datafile:
        return int(datafile.read().split()[1])


#the weights of the knapsack (weights)
def weights(file):
    w=np.loadtxt('ks_82_0')[1:, 1]
    return w.astype(int) #read them as int


#the vaues of knapsack (values)
def values(file):
    v=np.loadtxt('ks_82_0')[1:, 0]
    r=numpy.array(v)
    return r.astype(int) #read them as int



#Function knapsack takes capacity, weights, values and the length of values
def knapSack(C, wgts, val, l):
    #Create table of values from 0 to capacity +1 to len val +1
    TableVal = [[0 for w in range(C + 1)]
                   for i in range(l + 1)]

    #Loop though our table of values
    for i in range(l + 1): #i loops though the number of lists
        for j in range(C + 1):#j loops though the valeus of each list
            if j == 0 or i == 0:
                TableVal[i][j] = 0 #fill the tablaval with 0's

      #if the weights in position of the our table -1 is less than the value fo the list
            elif wgts[i - 1] <= j:
                #return in tableval the maximum comparation bewtween the sum of values and out table in
                #tableval[i-1][j], j goes up by one each iteration so we check all posible combinations
                TableVal[i][j] = max(TableVal[i - 1][j],val[i - 1] + TableVal[i - 1][j - wgts[i - 1]]
                          )
     #else since j is less than out weights, the next value has to be the [i-1][j]
            else:
                TableVal[i][j] = TableVal[i - 1][j]


    final = TableVal[l][C] #The final sum has to be in the last values of TableVal
    print(final)#print our final value
    global z #make z global to all of our funcitons
    z=[] #inizialize z
    j = C
    #total=sum(val) #the total sum of the values
    #z = [] #z array that has the knapSack
    #i is the len of the num values (l)
    for i in range(l, 0, -1):
        if final <= 0:
            break #if the final sum is 0, all numbers seen, break.

        #The result from our table has to be on (TableVal[i-1][j])
        # or is in the result of the sum of val[i-1] and TableVal[i-1] [j-wgts[i-1]])
        if  final == TableVal[i - 1][j]:
            continue
        else:
            # This item is included.
         #send the item to our z
            z.append(wgts[i - 1])

          #this value is taken from our final
            final = final - val[i - 1]
            j = j - wgts[i - 1]




#Main
#read th input file and call funciton on each number
readFile('ks_82_0')
C = capacity('ks_82_0')
val = values('ks_82_0')
wgts = weights('ks_82_0 ')
l = len(val)



knapSack(C, wgts, val, l)
#send file to output
sys.stdout=open("ks_82_0_output.txt","w")
knapSack(C, wgts, val, l)


#print 1 if the value is the one of our knapSack
for t in wgts:
        if any(t == z):
            print(1)
        else:
            print(0)
#sys.stdout.close()
