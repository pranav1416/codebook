class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        res = ""
        max = 0
        for char in s:
            try:
                my_dict[char]
                if(max<len(res)):
                    max = len(res)
                res = ""
                my_dict = {}
            except KeyError:
                res += char
                my_dict[char] = 1
        return max

if __name__ == "__main__":
    test_case = "pwwkew"
    sol = Solution()
    ans = sol.lengthOfLongestSubstring(test_case)
    print(ans)