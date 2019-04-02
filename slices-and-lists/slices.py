s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))


l = input().split()
print(max(l), min(l))
l = [i%2 for i in range(len(l))]
print(l)
l = [0 for i in range(len(l))]
l[0] = l[-1] = 1
print(l)
print(set([i for i in l if l.count(i)>1]))


s = input()
print(s[int(len(s)/2)-2:int(len(s)/2+2)])