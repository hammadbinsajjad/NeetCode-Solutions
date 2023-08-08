class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        st = set()
        max_len = 0
        n = len(s)

        while r < n and l < n:
            if l > r:
                r = l
            if s[r] not in st:
                # st.append(s[r])
                st.add(s[r])
            else:
                while l < n and s[l] != s[r]:
                    st.remove(s[l])
                    l += 1
                l += 1
            r += 1
            max_len = max(max_len, r - l)
        return max_len



