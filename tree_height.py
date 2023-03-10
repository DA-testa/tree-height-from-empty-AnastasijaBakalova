# python3
import sys
import threading
import numpy as np
flags = []
countRoute = []

def compute_height(n, parents, parent_children):
  #print(parents)
  if (flags[n]!=1):
    flags[n]=1;
    if (parents == -1):
      max_height = 1
      countRoute[n] = 1
      
    else :
      max_height = 1 + compute_height(parents, parent_children[parents], parent_children)
      countRoute[n] = max_height
    return max_height
  else :
    return countRoute[n]


def main():
    # implement input form keyboard and from files
    
   # let user input file name to use, don't allow file names with letter a
  try:
    readfrom = input()
    bool1 = False
    if ("I" in readfrom) or ("i" in readfrom) :
      bool1 = True
      count = int (input())
      parent_children = np.array([int(j) for j in input().split()])
      #print(parent_children[4])
      
    if ("F" in readfrom) or ("f" in readfrom):
      name = "test/"+input()
      if not("a" in name):
        bool1 = True
        with open(name) as file:
          count = int(next(file))
          #print(count)
          for line in file:
              parent_children= np.array(([int(j) for j in line.split()]))
          #print(parent_children)
    if bool1:  
      for i in range(0, count, 1) :
        flags.append(0)
        countRoute.append(0)
      max = 0
      #print(count)
      for i in range (0, count, 1):
        max2 = compute_height(i, parent_children[i], parent_children)
        if(max2>max):
          max= max2

      print(max)
  except Exception as inst:
    print(type(inst))  
    print(inst.args)    
    print(inst)
      
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
