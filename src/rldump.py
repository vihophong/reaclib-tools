import rlload as rl

infile = "results02090719.txt"

reaclib=rl.load_txt(infile)

rl.dump_txt(reaclib)
