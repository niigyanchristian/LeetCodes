def canPlaceFlowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0

        if len(flowerbed) == 1 and flowerbed[0] == 0:
           count = count+1
           return count >= n
        elif len(flowerbed) == 1 and flowerbed[0] == 1:
            return count >= n
        elif len(flowerbed) == 0:
            return count >= n   

        def check(m,l):
              if m ==0 and l == 0:
                    # count = count+1
                    return 1
              else:
                    return m

        a =check(flowerbed[0],flowerbed[1])
        if flowerbed[0] != a:
            count = count + 1
        flowerbed[0] = a
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                  flowerbed[i] = 1
                  count = count+1
        b =check(flowerbed[-1],flowerbed[-2])
        if flowerbed[-1] != b:      
            count = count + 1
        flowerbed[-1] = b
                  
        return count >= n     


print(canPlaceFlowers([1,0,0,0,1], 1))
