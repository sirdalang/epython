# slice

# L[m:n]
# start at index m, end before n
# [m, n)

l = list(range(10))

print (l)

nl = l[4:5] # slice

print(nl)

# using slice on strings
def my_trim(s):
    spacecount = 0
    for it in s:
        if it == ' ':
            spacecount += 1
        else:
            break

    s = s[spacecount:]

    spacecount = 0
    istrlen = len(s)
    for it in reversed(s):
        if it == ' ':
            spacecount += 1
        else:
            break
    
    s = s[:istrlen - spacecount]

    return s

s = my_trim ("  ha  ha  ")
print ("s=<%s>" % s)