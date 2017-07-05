# Excel Column-to-Number

def titleToNumber(self, s):
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))


 def titleToNumber(s):
    s = s[::-1]
    sum = 0
    for exp, char in enumerate(s):
        sum += (ord(char) - 65 + 1) * (26 ** exp)
    return sum

def titleToNumber(self, s):
   	result = 0
    for i in xrange(len(s)):
        result *= 26
        result += ord(s[i]) - ord('A') + 1
    return result