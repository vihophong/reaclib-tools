import matplotlib.pyplot as plt
from twopiece.scale import tpnorm
#import rlload as rl
import numpy as np
import sys

# print 'Number of arguments:', len(sys.argv), 'arguments.'
# print 'Argument List:', str(sys.argv)

# infile = "results02090719.txt"
#reaclib = rl.load_txt(infile)
#np.save("results02090719.npy",reaclib)

reaclib = np.load("results02090719.npy",allow_pickle='TRUE')

res0n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][1] and cond["nucZ"][0]==cond["nucZ"][1]-1 and cond["chap"] == 1),reaclib)
res1n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][2]+1 and cond["nucZ"][0]==cond["nucZ"][2]-1 and cond["chap"] == 2),reaclib)
res2n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][3]+2 and cond["nucZ"][0]==cond["nucZ"][3]-1 and cond["chap"] == 3),reaclib)
res3n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][4]+3 and cond["nucZ"][0]==cond["nucZ"][4]-1 and cond["chap"] == 11),reaclib)

def get_weak_rate(A, Z):
    w0n = filter(lambda cond: (cond["nucA"][0]==A and cond["nucZ"][0]==Z),res0n)
    w1n = filter(lambda cond: (cond["nucA"][0]==A and cond["nucZ"][0]==Z),res1n)
    w2n = filter(lambda cond: (cond["nucA"][0]==A and cond["nucZ"][0]==Z),res2n)
    w3n = filter(lambda cond: (cond["nucA"][0]==A and cond["nucZ"][0]==Z),res3n)
    return w0n,w1n,w2n,w3n

def change_weak_rate(A,Z,T12,Pxn,x):
    w0n,w1n,w2n,w3n = get_weak_rate(A,Z)
    if (x==0):
        for i in w0n:
            print("old = ",i)
            if (Pxn==0 or T12==0):
                i["rate"][0] = -9999
            else:
                i["rate"][0] = np.log(np.log(2)/T12*Pxn/100)
            print("new = ",i)
        
    if (x==1):
        for i in w1n:
            if (Pxn==0 or T12==0):
                i["rate"][0] = -9999
            else:
                i["rate"][0] = np.log(np.log(2)/T12*Pxn/100)
        print(i)
    if (x==2):
        for i in w2n:
            if (Pxn==0 or T12==0):
                i["rate"][0] = -9999
            else:
                i["rate"][0] = np.log(np.log(2)/T12*Pxn/100)
        print(i)
    if (x==3):
        for i in w3n:
            if (Pxn==0 or T12==0):
                i["rate"][0] = -9999
            else:
                i["rate"][0] = np.log(np.log(2)/T12*Pxn/100)
        print(i)

# for i in res0n:
#     if (not (i["label"]=="wc12" or i["label"]=="mo03")):
#         print(i)
change_weak_rate(128,52,0.14,35,0)
#test = list(filter(lambda cond: (cond["nucA"][0]==134 and cond["nucZ"][0]==49 and cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][1] and cond["nucZ"][0]==cond["nucZ"][1]-1 and cond["chap"] == 1),reaclib))
#print(test)
# dist = tpnorm(loc=100, sigmal=1.0, sigmar=2.0)
# sample = dist.random_sample(size = 500)
# print(sample)