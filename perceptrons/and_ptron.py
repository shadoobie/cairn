import numpy,random,os

lr = 1
bias = 1
weights = list()
for k in range(3):
    weights.append(random.random())  #Assigning random weights

def ptron(inp1,inp2,outp):
    outp_pn = inp1*weights[0]+inp2*weights[1]+bias*weights[2]
    outp_pn = 1.0/(1+numpy.exp(-outp_pn))   #Sigmoid Function
    err = outp - outp_pn
    weights[0] += err*inp1*lr   #Modifying weights
    weights[1] += err*inp2*lr
    weights[2] += err*bias*lr

for i in range(100):    #Training With Data
    ptron(0,0,0)     #Passing the tryth values of OR
    ptron(1,1,1)
    ptron(1,0,0)
    ptron(0,1,0)

for x,y in [(0,0),(1,0),(0,1),(1,1)]:
    outp_pn = x*weights[0]+y*weights[1]+bias*weights[2]
    #Based on the trained wieghts
    outp = 1.0/(1+numpy.exp(-outp_pn))
    print(str(x) + " AND " + str(y) + " yields: " + str(outp))