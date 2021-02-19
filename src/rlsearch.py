import rlload as rl

infile = "results02090719.txt"

reaclib=rl.load_txt(infile)

res = filter(lambda cond: (cond["nuc"][0] == "n" and cond["nuc"][1] == "p" and cond["chap"] == 1),reaclib)
print res