import rlload as rl
import matplotlib.pyplot as plt


infile = "results02090719.txt"

reaclib=rl.load_txt(infile)

res0n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][1] and cond["nucZ"][0]==cond["nucZ"][1]-1 and cond["chap"] == 1),reaclib)
res1n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][2]+1 and cond["nucZ"][0]==cond["nucZ"][2]-1 and cond["chap"] == 2),reaclib)
res2n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][3]+2 and cond["nucZ"][0]==cond["nucZ"][3]-1 and cond["chap"] == 3),reaclib)
res3n = filter(lambda cond: (cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][4]+3 and cond["nucZ"][0]==cond["nucZ"][4]-1 and cond["chap"] == 11),reaclib)

resall = filter(lambda cond: ((cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][4]+3 and cond["nucZ"][0]==cond["nucZ"][4]-1 and cond["chap"] == 11) or \
	(cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][3]+2 and cond["nucZ"][0]==cond["nucZ"][3]-1 and cond["chap"] == 3) or \
	(cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][2]+1 and cond["nucZ"][0]==cond["nucZ"][2]-1 and cond["chap"] == 2) or \
	(cond["rtype"]=="w" and cond["nucA"][0]==cond["nucA"][1] and cond["nucZ"][0]==cond["nucZ"][1]-1 and cond["chap"] == 1)),reaclib)
 

n_0n = []; z_0n = [] 
for index in range(len(res0n)):
	z_0n.append(res0n[index]["nucZ"][0])
	n_0n.append(res0n[index]["nucA"][0]-res0n[index]["nucZ"][0])
	#print res0n[index]["nuc"][0],res0n[index]["nuc"][1]

n_1n = []; z_1n = [] 
for index in range(len(res1n)):
	z_1n.append(res1n[index]["nucZ"][0])
	n_1n.append(res1n[index]["nucA"][0]-res1n[index]["nucZ"][0])
	#print res1n[index]["nuc"][0],res1n[index]["nuc"][1],res1n[index]["nuc"][2]

n_2n = []; z_2n = [] 
for index in range(len(res2n)):
	z_2n.append(res2n[index]["nucZ"][0])
	n_2n.append(res2n[index]["nucA"][0]-res2n[index]["nucZ"][0])
	#print res2n[index]["nuc"][0],res2n[index]["nuc"][1],res2n[index]["nuc"][2],res2n[index]["nuc"][3]

n_3n = []; z_3n = [] 
for index in range(len(res3n)):
	z_3n.append(res3n[index]["nucZ"][0])
	n_3n.append(res3n[index]["nucA"][0]-res3n[index]["nucZ"][0])
	#print res3n[index]["nuc"][0],res3n[index]["nuc"][1],res3n[index]["nuc"][2],res3n[index]["nuc"][3],res3n[index]["nuc"][4]


for index in range(len(resall)):
	print resall[index]["label"],resall[index]["nuc"][0],resall[index]["nuc"][1],resall[index]["nuc"][2],resall[index]["nuc"][3],resall[index]["nuc"][4]

x1 = 0; x2 = 240
y1 = 0; y2 = 115

plt.rcParams["figure.figsize"] = (5, 5)
plt.rcParams["font.size"] = 20

plt.xlim(x1,x2)
plt.ylim(y1,y2)

plt.xlabel('Neutron number, $N$')
plt.ylabel('Proton number, $Z$')

plt.plot(n_0n, z_0n, 's', markersize = 6, label = "p0n")
plt.plot(n_1n, z_1n, 's', markersize = 6, label = "p1n")
plt.plot(n_2n, z_2n, 's', markersize = 6, label = "p2n")
plt.plot(n_3n, z_3n, 's', markersize = 6, label = "p3n")


plt.legend()

plt.show()
