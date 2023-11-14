def numberOfEmployeesWhoMetTarget(hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        count = 0

        for i in hours:
            if i >= target:
                count = count+1
        return count



numberOfEmployeesWhoMetTarget([0,1,2,3,4],2)