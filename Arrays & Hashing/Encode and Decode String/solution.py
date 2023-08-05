class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        s = ""
        for st in strs:
            s += f"{st}\0"
        return s

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, s):
        # write your code here
        res = s.split("\0")
        res.pop()
        return res
        
s = Solution()
print(s.decode(s.encode(["we", "say", ":", "yes"])))