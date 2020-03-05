import sys

a = sys.stdin.readline()

for line in a:
       a, b, c = [int(i) for i in line.split()]
       print 'a = %d, b = %d, c = %d\n' %(a, b, c)