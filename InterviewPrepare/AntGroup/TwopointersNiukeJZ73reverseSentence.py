class Solution:
    def ReverseSentence(self, str: str) -> str:
        # write code here
        words = str.split()
        front = 0
        end = len(words)-1
        while front < end:
            words[front], words[end] = words[end], words[front]
            front += 1
            end -= 1
        return ' '.join(words)
