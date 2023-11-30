def reverse_vowels(s):
    array = list(s)
    vowels = set('aeiouAEIOU')
    frontIndex, endIndex = 0, len(array) - 1
    
    while frontIndex < endIndex:
        while frontIndex < endIndex and array[frontIndex].lower() not in vowels:
            frontIndex += 1
        while frontIndex < endIndex and array[endIndex].lower() not in vowels:
            endIndex -= 1
        array[frontIndex], array[endIndex] = array[endIndex], array[frontIndex]
        frontIndex += 1
        endIndex -= 1
    return ''.join(array)

# Example usage:
input_str1 = "ai."
print(reverse_vowels(input_str1))

input_str2 = "leetcode"
print(reverse_vowels(input_str2))
