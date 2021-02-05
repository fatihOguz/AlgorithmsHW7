import random
def partition(arr,low,high):
    i = ( low-1 )        
    pivot = arr[high]     
 
    for j in range(low , high):
 
       
        if   arr[j] <= pivot:
         
      
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
 
def quickSort(arr,low,high):
    if low < high:
 
      
        pi = partition(arr,low,high)
 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def solve(A,intervals):
    quickSort(A,0,len(A)-1)
    for i in intervals:
        print(str(A[i[0]]) + " " ,end = '')
    print()




###############################################################################################################################

## Make a 2D list
intervals=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for i in range(0,10):
    for j in range(0,2):
        if(j==0):
            intervals[i][j] = random.randint(1,10)
        else:
            intervals[i][j] = random.randint(1,intervals[i][0])
        #print(str(intervals[i][j]) + " " , end = '')
    #print()


for i in range(0,10):
    temp=intervals[i][1] 
    intervals[i][1]=intervals[i][0]
    intervals[i][0]=temp 
    

#print(intervals)

## Make a A list
A=[0,0,0,0,0,0,0,0,0,0]
for i in range(0,10):
    A[i]=random.randint(1,10)

#quick sort for A

print(intervals)
print(A)


solve(A,intervals)

    
