import time
from numpy.random import randint
import matplotlib.pyplot as plt

def mergesort(array):
    if len(array)>1:
       
        r=len(array)//2
        L=array[:r]
        M=array[r:]
        mergesort(L)
        mergesort(M)
        i=j=k=0
       
        while i<len(L) and j<len(M):
            if L[i]<M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1
           
        while i<len(L):
            array[k]  =L[i]
            i+=1
            k+=1
        while j<len(M):
            array[k]=M[j]
            j+=1
            k+=1
def read_input():
    a=[]      
    n=int(input("Enter the number of tv channels:"))
    print("enter the number of viewers:")
    for i in range(0,n):
        l=int(input())
        a.append(l)
               
    return a
elements=list()
times=list()
global labeldata
print("1.Merge sort 2. Quick sort 3. Selection sort")
array=read_input()
mergesort(array)
labeldata="Merge Sort"
print("Sorted array is:")
print(array)


    
print("-----------------Running time analysis------------------")
for i in range(1,11):
    array=randint(0,1000*i,1000*i)
    start=time.time()
    
    mergesort(array)
   
        
    end=time.time()
    print(len(array),"elements sorted by",labeldata,end-start)
    elements.append(len(array))
    times.append(end-start)
plt.xlabel('list length')
plt.ylabel('time complexity')
plt.plot(elements,times,label=labeldata)
plt.grid()
plt.legend()
plt.show()