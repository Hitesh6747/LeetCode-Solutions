class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        siz=len(nums)
        neg=[]
        pos=[]
        res=[]
        i=0
        while i < siz:
            if nums[i]>=0:
                pos.append(nums[i])
                i+=1
            else:
                neg.append(nums[i])
                i+=1
        if (len(neg)==0):
            return [x*x for x in pos]
        if (len(pos)==0):
            res= [x*x for x in neg]
            res.reverse()
            return res 
           
        x=0
        y=0
        neg=[x*x for x in neg][::-1]           
        pos=[x*x for x in pos]
        while x<len(neg) and y<len(pos):
            if neg[x]<=pos[y]:
                res.append(neg[x])
                x+=1
            else:
                res.append(pos[y])
                y+=1
        while x<len(neg):
            res.append(neg[x])
            x+=1
        while y<len(pos):
            res.append(pos[y])
            y+=1
        return res

            
                
        