class Solution:
    def minimumAbsDifference(self, arr: [int]) -> [[int]]:
        arr.sort()
        min_abs = arr[1] - arr[0]

        for i in range(len(arr) - 1):
            min_abs = min(min_abs, arr[i+1] - arr[i])
            
        res = []
        for i in range(len(arr) - 1):
            if arr[i+1]-arr[i] == min_abs:
                res.append([arr[i], arr[i+1]])
        return res    

        
        
