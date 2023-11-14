def selfDividingNumbers(left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        start = left
        end = right
        result = []
        while(start<end+1):
            count = 0
            for i in str(start):
                print(i)
                if int(i) != 0:    
                    if start % int(i) == 0:
                        count = count + 1
            if count == len(str(start)): 
                result.append(start)
            start = 1 + start
        return result
            



print(selfDividingNumbers(48,85))