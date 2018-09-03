import glob

a  = glob.iglob("*")
print a

for path in a : 
    print path
