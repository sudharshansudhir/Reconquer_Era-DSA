class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
        print(dict)
        ans=[]
        for kk,v in dict.items():
            ans.append([v,kk])
        ans.sort()
        ans=ans[::-1]
        a=[]
        for i in ans:
            a.append(i[1])
        print(a,k)
        return a[:k]