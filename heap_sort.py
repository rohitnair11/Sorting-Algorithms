class Solution:

    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def left(self,i):
        return (2*i +1)
    
    def right(self,i):
        return (2*(i+1))

    def max_heapify(self,i,n):
        l = Solution.left(self,i)
        r = Solution.right(self,i)
        if(l < n):
            self.comparison_count+=1
        if(l<n and self.sorting_array[l]>self.sorting_array[i]):
            largest = l
        else:
            largest = i
        if(r < n):
            self.comparison_count+=1
        if(r<n and self.sorting_array[r]>self.sorting_array[largest]):
            largest = r
        if largest != i:
            temp = self.sorting_array[i]
            self.sorting_array[i] = self.sorting_array[largest]
            self.sorting_array[largest] = temp
            Solution.max_heapify(self,largest,n)


    def build_max_heap(self,n):
        for i in range((len(self.sorting_array)/2)-1,-1,-1):
            Solution.max_heapify(self,i,n)

    def heap_sort(self):
        n = len(self.sorting_array)
        Solution.build_max_heap(self,n)
        for i in range(n-1,0,-1):
            temp = self.sorting_array[i]
            self.sorting_array[i] = self.sorting_array[0]
            self.sorting_array[0] = temp
            n = n - 1
            Solution.max_heapify(self,0,n)
            
        print("Sorted Array : ") 
        print(self.sorting_array)
        print("Number of comparisons : ")
        print(self.comparison_count)