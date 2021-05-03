class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        hashdict = dict()
        s = list(s)
        start = 0
        end = 0
        length = 1
        while(end<len(s) and start<len(s)):
            if end == len(s)-1:
                if s[end] in s[start:end]:
                    li = end - start
                    length = max(length, li)
                else:
                    li = end+1 - start
                    length = max(length, li)
                break

            else:
                if s[end] in s[start:end]:
                    li = end - start
                    length = max(length, li)
                    start = hashdict[s[end]] + 1

                hashdict[s[end]] = end
                end += 1

        return length







S3 = Solution3
S3.lengthOfLongestSubstring(S3,"abb")
