fname = input('Enter a file name:\n')
fhandle = open(fname,'r')
for line in fhandle:
    line = line.upper()
    print(line)


