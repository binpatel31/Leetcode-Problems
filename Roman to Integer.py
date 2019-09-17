import math
class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'min':0}
        s_integer = list(map(lambda x: dict[x],list(s)) )
        integer = 0
        mini = s_integer[0]
        for ind in range(len(s_integer)):
            if s_integer[ind] > mini:
                integer=integer-s_integer[ind-1]+(s_integer[ind]-s_integer[ind-1])
                mini = s_integer[ind]
            else:
                mini = s_integer[ind]
                integer+=s_integer[ind]
        return integer