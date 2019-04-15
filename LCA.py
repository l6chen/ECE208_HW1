#!/usr/bin/env python3

def find_LCAs(parent):
    LCA = dict() # This is the nested dictionary you will be modifying

    # TODO You will fill in the following "lca" function
    def lca(u, v):
        '''
        This function computes the Least Common Ancestor between nodes u and v
        :param u: node u
        :param v: node v
        :return: A set containing the LCAs of u and v
        '''
        
            
        if u not in LCA:
            LCA[u] = {}
            
        if v not in LCA[u]:
            LCA[u][v] = set()
        elif LCA[u][v] != set():
            return LCA[u][v]
            
        if u == v:
            LCA[u][v].add(u)
        
        for pv in parent[v]:
            LCA[u][v] = LCA[u][v] | lca(u,pv) 
        
        for pu in parent[u]:
            LCA[u][v] = LCA[u][v] | lca(pu,v)
            
        for pu in parent[u]:
            for pv in parent[v]:
                LCA[u][v] = LCA[u][v] | lca(pu,pv)
        
        subtract = set()
        for a in LCA[u][v]:
            for b in LCA[u][v]:
                if a != b and lca(a,b) != set():
                    subtract = subtract | lca(a,b)
        
        
        LCA[u][v] -= subtract 
        
        return LCA[u][v] 


    # Now, we will call your recursive "lca" function on all pairs of nodes to populate the "LCA" dictionary
    for u in parent:
        for v in parent:
            lca(u,v)

    return LCA

if __name__ == "__main__":
    '''
    This is how we handle loading the input dataset, running your function, and printing the output
    '''
    from sys import argv
    if len(argv) != 2:
        print("USAGE: %s <parent_dictionary>" % argv[0]); exit(1)
    from ast import literal_eval
    parent = literal_eval(open(argv[1]).read())
    print(find_LCAs(parent))
