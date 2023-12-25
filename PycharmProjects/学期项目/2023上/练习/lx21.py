from sys import stdout
for i in range(4):
    for a in range(2-i+1):
        stdout.write(" ")
    for b in range(2*i+1):
        stdout.write("*")
    print(" ")
for j in range(3):
    for x in range(j+1):
        stdout.write(" ")
    for y in range(4-2*j+1):
        stdout.write("*")
    print("")
