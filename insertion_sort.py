class Solution:

	def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

	def insertion_sort(self):
        for i in range(1,len(self.sorting_array)):
            j = i-1
            key = self.sorting_array[i]
            self.comparison_count += 1
            while(j>=0 and self.sorting_array[j]>key):
                self.sorting_array[j+1] = self.sorting_array[j]
                self.comparison_count += 1
                j -= 1
                if(j==-1):
                    self.comparison_count -=1
            self.sorting_array[j+1] = key
        print("Sorted Array : ") 
        print(self.sorting_array)
        print("Number of comparisons : ")
        print(self.comparison_count)