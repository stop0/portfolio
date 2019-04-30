# N input with numbers precedding it
# Ex. N = 3 , 1 2 3
a = []
n = int(input())
c = 0
while c != n:
    c = c + 1
    a.append(c)

s = ''.join(map(str, a))

print(s)
