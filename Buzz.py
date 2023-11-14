def fizzBuzz(n):
        result =[]
        for i in range(n):
            var = str(i+1)
            if (i+1)%3 == 0 and (i+1)%5 == 0:
                var = "FizzBuzz"
            elif (i+1)%3 == 0:
                var = "Fizz"
            elif (i+1)%5 == 0:
                var = "Buzz"
            result.append(var)
        return result


print(fizzBuzz(15))