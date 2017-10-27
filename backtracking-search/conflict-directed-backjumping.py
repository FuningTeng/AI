from collections import deque
class node:
    def __init__(self, val):
        self.val = val
        self.conflictSet = deque() 
        self.neighbors = set() # connected node
        self.D = [] # doamin
        self.color = ''
    def inference(self, csp):
        for node in self.conflictSet:
            if (csp.DN[node]).color == self.color:
                print 'conflict with ' + node
                return False
        return True
class CSP:
    def __init__(self, dn, l):
        self.DN = dn
        self.L = l

def backtracking_search(csp):
    backtrack(0, csp)
# assignment: Tuple list
# index: assignment index
def backtrack(index, csp):
    if index == len(csp.L):
        return True
    unassiged = (csp.L)[index]
    for color in csp.DN[unassiged].D: 
        csp.DN[unassiged].color = color
        stringExpanding = unassiged + ' = ' + color
        print stringExpanding
        if (csp.DN[unassiged]).inference(csp):
            result = backtrack(index + 1, csp)
            if result:
                return result
        csp.DN[unassiged].color = ''
    return False

import ast

L = [] # list order
DX = {} 
DN = {} # dictonary of nodes

with open('graph-weighted.txt', 'r') as f:
    for line in f:
        cur = str(line.split())[2:-2]
        s=cur[0]
        if s is 'L':
            cur=cur[2:]
            L = ast.literal_eval(cur)
        else:
            c = ast.literal_eval(cur)
            DX.update(c)
D = []
D.append('R')
D.append('G')
D.append('B')
for key, value in DX.iteritems():
    n = node(key)
    n.conflictSet = deque(value)
    n.neighbors = set(value)
    n.D = D
    DN[n.val] = n

backtracking_search(CSP(DN, L))
stringExpanding = ''
for key, item in DN.iteritems():
    stringExpanding += item.val + ' = ' + item.color + ', '
print stringExpanding[:-2]