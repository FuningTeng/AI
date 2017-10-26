from collections import deque
class node:
    def __init__(self, val):
        self.val = val
        self.conflictSet = deque()
        self.neighbors = set()

import ast

L = []
DX = {}
DN = []

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

for key, value in DX.iteritems():
    n = node(key)
    n.conflictSet = deque(value)
    n.neighbors = set(value)
    DN.append(n)