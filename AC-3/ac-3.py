# Source: https://en.wikipedia.org/wiki/AC-3_algorithm
#  Input:
#    A set of variables X
#    A set of domains D(x) for each variable x in X. D(x) contains vx0, vx1... vxn, the possible values of x
#    A set of binary constraints C(x, y) on variables x and y that must be satisfied
   
#  Output:
#    Arc consistent domains for each variable.
class node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

from collections import deque

# CSP with n variables,
# each with domain size at most d, and with c binary constraints (arcs). Each arc (Xk,Xi) can
# be inserted in the queue only d times because Xi has at most d values to delete
# Checking consistency of an arc can be done in O(d^2) time, 
# so we get O(cd^3) total worst-case time
def Arc_3(queue, C, DX):
    while queue:
        x = queue.popleft()
        stringExpanding = 'Remove ' + str(x) 
        print(stringExpanding)    
        if revise(x, DX):
            if len(DX[x[0]]) == 0:
                print 'Domain is empty'
                return False
            for y in C[x[0]].neighbors:
                if y != x[1]:
                    queue.append((y,x[0]))
                    stringExpanding = 'Add ' + str((y,x[0])) + ' to queue'
                    print(stringExpanding)    
    return True

def revise(xTuple, DX):
    revised = False
    for x in DX[xTuple[0]]:
        allow = False
        for y in DX[xTuple[1]]:
            if x != y:
                allow = True
                break
        if not allow:
            DX[xTuple[0]].remove(x)
            stringExpanding = 'Delete ' + str(x) + ' From ' + xTuple[0]
            stringExpanding += ', leaving D(' + xTuple[0] + ') = ' + str(DX[xTuple[0]])
            print(stringExpanding)    
            revised = True
    return revised

import ast
C = {}
queue = deque()
X = []
D = []
with open('graph-weighted.txt', 'r') as f:
    for line in f:
        cur = str(line.split())[2:-2]
        s=cur[0]
        if s is 'X':
            cur=cur[2:]
            X = ast.literal_eval(cur)
        elif s is 'D':
            cur=cur[2:]
            D = ast.literal_eval(cur)
        else:
            c = ast.literal_eval(cur)
            queue.append(c)       
            queue.append((c[1], c[0]))      
            if C.has_key(c[0]):
                C[c[0]].neighbors.append(c[1])
            else:
                C[c[0]] = node(c[0])
                C[c[0]].neighbors.append(c[1])
            if C.has_key(c[1]):
                C[c[1]].neighbors.append(c[0])
            else:
                C[c[1]] = node(c[1])
                C[c[1]].neighbors.append(c[0])
DX = {}
for x in X:
    DX[x] = list(D)
DX['WA'] = ['G']
DX['V'] = ['R']
Arc_3(queue,C, DX)
print DX