f = open("hello.txt","r")
lines = f.readlines()
print lines
print len(lines)
f.close()
for n, val in enumerate(lines):
   globals()["var%d"%n] = val

print var0.rstrip()
print var1.rstrip()
print var2.rstrip()
