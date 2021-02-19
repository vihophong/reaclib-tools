import rlload as rl

infile = "results02090719.npy"

reaclib=rl.load_bin(infile)

res = filter(lambda cond: (cond["nuc"][0] == "n" and cond["nuc"][1] == "p" and cond["chap"] == 1),reaclib)
print res