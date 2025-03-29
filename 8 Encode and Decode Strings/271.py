class Solution:
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self,str): #  4#lint4#code
        res, i = [], 0

        while i< len(str):
            j = i
            while str[j] != '#':
                j+=1 # j = 1
            #slice a string and convert it into integar number
            #[0,1] -> length = 4
            length = int(str[i:j]) 
            res.append(str[j+1: j+1+length]) #[2,6]
            i = j+1+length # i = 6
        return res
    
strs = ["lint", "code", "love", "you"]
solution = Solution()
encoded_str = solution.encode(strs)
print(f"Encoded string: {encoded_str}")
decoded_strs = solution.decode(encoded_str)
print(f"Decoded strings: {decoded_strs}")

'''
Time Complexity: O(n∗k) for both encode and decode, where n is the number of strings and k is the average string length.
Space Complexity: O(n∗k) for both encode and decode.'
'''