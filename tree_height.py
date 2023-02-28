# python3

import sys
import threading
import numpy
list = []
flags = []
countRoute = []

def compute_height(n, parents, parent_children):
  #print(parent_children)
  if (flags[n]!=1):
    flags[n]=1;
    if (parents == -1):
      max_height = 1;
      countRoute[n] = 1;
      
    else :
      max_height = 1 + compute_height(parents, parent_children[int(parents)], parent_children)
      countRoute[n] = max_height
    return max_height
  else :
    return countRoute[n]


def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
  readfrom = input()
  if ("I" in readfrom) or ("i" in readfrom) :
    count = int (input())
    parent_children = [int(j) for j in input().split()]
    #print(parent_children[4])
    for i in range(0, count, 1) :
      list.append(i)
      flags.append(0)
      countRoute.append(0)
  if ("F" in readfrom) or ("f" in readfrom):
    name = input()
    file = open(name)
    count = int(file.readline)
    parent_children = [int(j) for j in file.readline.split()]



  max = 0
  for i in range (0, count, 1):
    max2 = compute_height(i,parent_children[i], parent_children)
    if(max2>max):
      max= max2
  print(max)
sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
