W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
class node:
    def __init__(self, state, estimate=0, cost=0, source=None):
        self.state = state
        self.cost = cost
        self.estimate = estimate
        self.source = source
    def printString(self):
        return "(" + self.state +", " + ("None" if self.source is None else self.source.state) + ", "+ str(self.cost) + ", "+  str(self.estimate) + ")"
    def __cmp__(self, other):
            return cmp(self.estimate, other.estimate)


class SimpleGraph:
    def __init__(self):
        self.edges = {}
        self.heuristic = {}

    def neighbors(self, id):
        return self.edges[id]

import heapq
class PriorityQueue:
    '''Priority queue is just an envelope of a binary heap. see descirption at https://docs.python.org/2/library/heapq.html'''
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def reOrder(self):
        heapq.heapify(self.elements)

    def put(self, item):
        heapq.heappush(self.elements, item)

    def get(self):
        return heapq.heappop(self.elements)

    def __cmp__(self, other):
            return cmp(self.estimate, other.estimate)

from sets import Set

def Is_Consistent_Admissable(graph, start):
    list = graph.heuristic
    est = list.get(start)
    start_n = node(start,est, 0, None)
    frontier = PriorityQueue()
    frontier.put(start)
    closed = dict()
    while not frontier.empty():
        current_s = frontier.get()    
        closed[current_s] = 1
        for next in graph.neighbors(current_s):
            h =  list.get(current_s)
            c = next[1]
            hstar = list.get(next[0])
            if h > c + hstar:
                stringExpanding = 'h(' + current_s + ') = ' + str(h) + ' > '
                stringExpanding += '(c(' + current_s + ',' + next[0] + ') = ' + str(c) + ') + ('
                stringExpanding += 'h(' + next[0] + ') = ' + str(hstar) + ')'
                print(stringExpanding)                        
            if next[0] not in closed.keys():
                closed[next[0]] = 1
                frontier.put(next[0])     

def A_star_search(graph, start, goal):
    '''create node for initial state 'start': find its heuristic by key (state) in heuristic list (grpah.heuristic)'''
    list = graph.heuristic
    est = list.get(start)
    start_n = node(start,est, 0, None)
    frontier = PriorityQueue()
    frontier.put(start_n)
    closed = dict()
    stringExpanding = 'None | '
    stringExpanding += 'None' if frontier.empty() else reduce((lambda x, y: (x + ',' + y)), [x.printString() for x in frontier.elements]) 
    stringExpanding += ' | 0' 
    print(stringExpanding)   
    while not frontier.empty():
        current = frontier.get()    
        if current.state == goal:
            stringExpanding = current.printString() + ") | "
            stringExpanding += 'None' if frontier.empty() else reduce((lambda x, y: (x + ',' + y)), [x.printString() for x in frontier.elements]) 
            stringExpanding += ' | ' + str(current.cost)
            print(stringExpanding)  
            cost=current.cost
            # print the graph search path back
            result = []
            cur = current
            result.append(cur.state)
            while cur.source is not None:
                cur = cur.source
                result.append(cur.state)    
            result.reverse()
            # Print path from goal to destination        
            resultPrintString = reduce((lambda x, y: x + '->' + y), result)         
            print("%s\ncost of goal %s is %r" % (resultPrintString, goal, cost))
            #printing string variable %s and %r real vaiable
            break
        current_s = current.state
        closed[current_s] = current
        for next in graph.neighbors(current_s):
            cst = current.cost + next[1]
            est = list.get(next[0])+cst
            next_n = node(next[0], est, cst, current)      
            if next[0] in closed.keys():
                if closed[next[0]].estimate <= est:
                    continue
                else:
                    stringExpanding = '----updating: ' + closed[next[0]].printString()                  
                    closed[next[0]].estimate = est
                    closed[next[0]].cost = cst
                    closed[next[0]].source = current
                    stringExpanding += '->' + closed[next[0]].printString()
                    stringExpanding += ':'
                    frontier.reOrder()
                    print(stringExpanding)
            else:
                closed[next[0]] = next_n
                frontier.put(next_n)     

        stringExpanding = current.printString() + ") | "
        stringExpanding += 'None' if frontier.empty() else reduce((lambda x, y: (x + ',' + y)), [x.printString() for x in frontier.elements]) 
        stringExpanding += ' | ' + G + str(current.cost) + W
        print(stringExpanding)    

import ast
y = {}
z = {}
with open('graph-weighted.txt', 'r') as f:
    for line in f:
        cur = str(line.split())[2:-2]
        s=cur[0]
        if s is 'h':
            cur=cur[2:]
            d1 = ast.literal_eval(cur)
            z.update(d1)
        else:
            d = ast.literal_eval(cur)
            y.update(d)

example_graph = SimpleGraph()
example_graph.edges = y
example_graph.heuristic = z
start = 'A' # raw_input('Starting point: ')
goal = 'R' # raw_input('Goal: ')
Is_Consistent_Admissable(example_graph,start)
A_star_search(example_graph,start,goal)
exit()