class Solution(object):
    def replaceDigits(self, s):
        str=''
        for i in range(len(s)):
            if "0"<=s[i]<="9":
              c=chr(ord(s[i-1])+int(s[i]))
              str=str+c
            else:
              str=str+s[i]
        return str