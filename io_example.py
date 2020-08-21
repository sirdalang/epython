f = open('test.file', 'w')

print (f.closed)

str = ['today', 'yesterday', 'tomorrow']

for s in str:
    f.write(s + '\n')

f.close()


f = open ('test.file', 'r')

lines = f.read()
print(lines)

f.close()