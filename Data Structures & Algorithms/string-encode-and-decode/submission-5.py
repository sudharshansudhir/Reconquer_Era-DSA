class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "ffalse"
        s=("#0").join(strs)
        return s
        

    def decode(self, s: str) -> List[str]:
        if s=="ffalse":
            return []

        ans=[]
        ans=s.split("#0")
        return ans
        