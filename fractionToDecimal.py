class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator==0:
            return str(numerator//denominator)
        flag = False
        s = str(numerator//denominator)
        remainder = numerator % denominator
        hashmap = set()
        s1 = ''
        while True:
            if remainder in hashmap:
                needed = str(remainder)
                flag = True
                break
            if remainder == 0:
                break
            if remainder*10 // denominator == 0:
                if '0' in s1:
                    needed = str(0)
                    flag = True
                    break
                s1 += str(0)
                remainder = remainder*10
                continue
            hashmap.add(remainder)
            remainder = remainder*10
            quotient = remainder//denominator
            remainder = remainder % denominator
            s1 += str(quotient)
        if flag == True:
            # this means that it is recurring
            # at the 'needed' number
            i = s1.find(needed)
            # we need to insert open before this index
            if i == 0:
                s1 = '(' + s1 + ')'
            else:
                s1 = s1[:i] + '(' + s1[i:] + ')'
        return(s+'.'+s1)


s = Solution()
s.fractionToDecimal(1, 2)