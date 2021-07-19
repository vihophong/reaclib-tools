import rlload as rl

#infile = "results02090719.txt"
infile = "results07190255.txt"

reaclib=rl.load_txt(infile)

#rl.dump_txt(reaclib)
#rl.convert(infile,"results02090719.txt")
rl.convert(infile,"results07190255.npy")