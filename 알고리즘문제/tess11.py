import sys

n=sys.stdin.readline().strip()

out=n[1:len(n)-1]
out=out.split(',')
print(type(out))
