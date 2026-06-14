class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=[]
        seen=[]
        for i in range (len(nums)):
            key=nums[i]
            if key in seen:
                continue
            seen.append(key)
            count=0

            for j in range (len(nums)):
                if nums[j]==key:
                    count+=1
            f.append([key,count])
            f.sort(key=lambda x: x[1], reverse=True) #When sorting, use the second element of each row
            #if i wanna sort by lowest frequency 1st
            #f.sort(key=lambda x: x[1])
        return [pair[0] for pair in f[:k]] #pair[0]= key value 






        