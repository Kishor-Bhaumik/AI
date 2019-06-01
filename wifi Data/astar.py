import operator
from collections import OrderedDict

children=[]
graph=[]
explored=[]

weight={}
F={}

block=[(2,2),(4,2),(2,3),(3,3),(3,5),(4,5)]
source=(3,1)
destination=(3,4)

weight.update({source:0})

def get_h(source):
    h=abs(source[0]-destination[0])+abs(source[1]-destination[1])
    return h
        

h=get_h(source)
F.update({source:h})
 
a=list(F.keys())[0]


def create_graph(heighest_rows,heighest_col):
    

    for i in range (1,heighest_rows+1):
        for j in range(1,heighest_col+1):
            a=(j,i)
            graph.append(a)
    return graph


def sortbyw(dicti):
    a=sorted(dicti.items(),key=lambda t: t[1])
    sorted_dict = OrderedDict(a)
    return sorted_dict
    

def distance_from_parent(child,source):

    if(abs(source[0]-child[0])==1):
        d=2
     
    if(abs(source[1]-child[1])==1):
        d=1

    return d
            
row=5
col=6
graph=create_graph(col,row)

gra=set(graph)-set(block)
new_graph=list(gra)

def get_children(source,graph):
    
    
    children.append((source[0]+1,source[1]))
    children.append((source[0]-1,source[1]))
    children.append((source[0],source[1]+1))
    children.append((source[0],source[1]-1))
    
    p=set(new_graph) & set(children)
    pp=list(p)
    return pp



empty={source:(source)}

while True:
        
    parent=list(F.keys())[0]
    
    children=get_children(parent,graph)
    if len(children)>0:
        for child in children:
            if child not in explored:
                h=get_h(child)
                weight_of_parent_from_source=weight.get(parent)
                g=weight_of_parent_from_source+distance_from_parent(child,parent)
                weight.update({child:g})
                f_score=g+h
                F.update({child:f_score})
                empty.update({child: (empty.get((parent)),child)})
                
                
            explored.append(child)  
                
                
          
    children=[]
    F.pop(parent,None)
    sortbyw(F)
    
            
    
    if (list(F.keys())[0]==destination):
        break
        
#cost=F.get(list(F.keys())[0])
cost=weight.get(destination)
path=empty.get(destination)

print("The path from {} to {} is {} and total cost is {}".format(source,destination,path,cost))