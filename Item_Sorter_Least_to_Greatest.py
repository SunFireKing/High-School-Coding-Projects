#List sorter and Duplicate remover
l = [8,5,7,6,4,-3,54,52,3,5,1,5,6,7,8,9]

def dupliremove(l):
  for i in l:
    count = l.count(i)
    if count > 1:
      for num in range(count-1):
        l.remove(i)
def sorter(l):
  for i in l:
    ilessthan = True  
    while ilessthan == True:
      if l.index(i) == 0:
        ilessthan = False
      elif l[l.index(i)] < (l[l.index(i) - 1]):
        nindex = l.index(i)
        l.remove(i)
        l.insert(nindex - 1, i)
      elif l[l.index(i)] > (l[l.index(i) - 1]):
        ilessthan = False
      elif l[l.index(i)] == l[0]:
        ilessthan = False
def rsorter(l):
  for i in l:
    igreatthan = True
    while igreatthan == True:
      if l.index(i) == 0:
        igreatthan = False
      elif l[l.index(i)] > (l[l.index(i) - 1]):
        nindex = l.index(i)
        l.remove(i)
        l.insert(nindex - 1, i)
      elif l[l.index(i)] < (l[l.index(i) - 1]):
        igreatthan = False
      elif l[l.index(i)] == l[0]:
        igreatthan = False
#def 

      

dupliremove(l)    
sorter(l)   

      
      

      

print(l)
l.sort()
print(l)



      
    
    

      
      
      
#I want to sort a numeric list
#First I create a loop for the entirety of the list
#The list should compare its self to the indexes infront, and if larger than an index, it will be appended infront of it

      
  
