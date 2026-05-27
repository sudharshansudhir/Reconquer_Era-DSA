class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in strs:
            arr=[0]*26
            for each in i:
                arr[ord(each)-97]=arr[ord(each)-97]+1
            print(arr)
            s=tuple(arr)
            print(s)
            if s not in dict.keys():
                dict[s]=[i]
            else:
                dict[s].append(i)
        ans=[]
        for k,v in dict.items():
            ans.append(v)
        return ans