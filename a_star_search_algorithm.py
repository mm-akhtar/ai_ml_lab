# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:13:35 2021

@author: akhtar
"""

class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
        
    def get_neighbors(self, v):
        return self.adjac_lis[v]
    
    #This is heuristic function which is having equal values for all nodes
    def h(self, n):
        keys = adjac_lis.keys()
        H = {}
        for x in keys:
            H[x] = 1
            
        H[chr(ord(list(H)[-1]) + 1)] = 1
        return H[n]
    
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        close_lst = set([])
        
        # poo has present distances from start to all other nodes
        # the default value is +infinity
        poo = {}
        poo[start] = 0
        
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
        
        while len(open_lst) > 0 :
            n = None
            for v in open_lst:
                # it will find a node with the lowest value of f() -
                if n == None or poo[v] + self.h(v) < poo[n] + self.h(n):
                    n = v
                    
            if n == None:
                print('path does not exisits!')
                return None
            
            if n == stop:
                reconst_path = []
                
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
                    
                reconst_path.append(start)
                reconst_path.reverse()
                
                print('path found {}' .format(reconst_path))
                return reconst_path
            
            for (m, weight) in self.get_neighbors(n):
                if m not in open_lst and m not in close_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                    
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
                        
                        if m in close_lst:
                            close_lst.remove(m)
                            open_lst.add(m)
                            
            open_lst.remove(n)
            close_lst.add(n)
            
        print('path does not exist')
        return None

adjac_lis = {
    'A': [('B', 1), ('C', 3), ('D', 4)],
    'B': [('D', 2)],
    'C': [('D', 1)],
    'D': [('B', 4), ('E', 1)],
    'E': [('D', 3)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'D')
        