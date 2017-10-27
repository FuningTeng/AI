from collections import deque
class node:
    def __init__(self, val):
        self.val = val
        self.conflictArray = []
        self.conflictSet = set()
        self.neighbors = set() # connected node
        self.D = [] # doamin
        self.color = ''
    def inference(self, csp):
        for node in self.neighbors:
            if (csp.DN[node]).color == self.color:
                print 'conflict with ' + node
                if node not in self.conflictSet:
                    self.conflictSet.add(node)
                    self.conflictArray.append(node)                  
                return False
        return True
class CSP:
    def __init__(self, dn, l):
        self.DN = dn
        self.L = l

def conflict_directed_backjumping(csp):
    backtrack(0, csp)
# assignment: Tuple list
# index: assignment index
def backtrack(index, csp):
    if index == len(csp.L):
        return (True, None)
    unassiged = (csp.L)[index]
    for color in list(csp.DN[unassiged].D): 
        csp.DN[unassiged].color = color
        stringExpanding = unassiged + ' = ' + color
        print stringExpanding
        if (csp.DN[unassiged]).inference(csp):
            result = backtrack(index + 1, csp)
            if result[0]:
                return (True, None)
            elif result[1] is not None:                 
                if result[1] != unassiged:
                    return result
        csp.DN[unassiged].color = ''
    if(len(csp.DN[unassiged].conflictArray) > 0):
        stringExpanding = unassiged + '\'s conflict set = ' + str(csp.DN[unassiged].conflictArray)
        lastConflict = csp.DN[unassiged].conflictArray[len(csp.DN[unassiged].conflictArray) - 1]
        index = csp.L.index(lastConflict)
        stringExpanding += '\n' + lastConflict + '\'s conflict set ' + str(csp.DN[lastConflict].conflictArray)
        for item in csp.DN[unassiged].conflictArray:
            if item not in csp.DN[lastConflict].conflictSet and item != csp.DN[lastConflict].val:
                csp.DN[lastConflict].conflictSet.add(item)
                csp.DN[lastConflict].conflictArray.append(item)
        stringExpanding +=  '\n      So conflict set for ' + lastConflict + ' is: ' + str(csp.DN[lastConflict].conflictArray)
        stringExpanding += ', jump to ' + lastConflict
        print stringExpanding
        return (False, lastConflict)
    return (False, None)

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
    n.neighbors = set(value)
    n.D = list(D)
    DN[n.val] = n

conflict_directed_backjumping(CSP(DN, L))
stringExpanding = ''
for key, item in DN.iteritems():
    stringExpanding += item.val + ' = ' + item.color + ', '
print stringExpanding[:-2]