class Solution:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge(self,p,q,r):
        n1 = q-p+1
        n2 = r-q
        L=[0 for i in range(n1+1)]
        R=[0 for i in range(n2+1)]
        for i in range(n1):
            L[i] = self.sorting_array[p+i]
        for j in range(n2):
            R[j]= self.sorting_array[q+j+1]
        L[n1] = float("inf")
        R[n2] = float("inf")
        i = 0
        j = 0
        for k in range(p,r+1):
            self.comparison_count +=1
            if(L[i]<R[j]):
                self.sorting_array[k] = L[i]
                i +=1
            else:
                self.sorting_array[k] = R[j]
                j+=1


    def merge_sort(self, p, r):
        if p<r:
            q = (p+r)/2
            Solution.merge_sort(self,p,q)
            Solution.merge_sort(self,q+1,r)
            Solution.merge(self,p,q,r)
            
        print("Sorted Array : ") 
        print(self.sorting_array)
        print("Number of comparisons : ")
        print(self.comparison_count)