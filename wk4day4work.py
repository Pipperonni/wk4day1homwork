# Exercise #1 
# Reverse the list below in-place using an in-place algorithm.
# For extra credit: Reverse the strings at the same time.

words = ['this' , 'is', 'a', 'sentence', '.']

def reverse_rev(input):
    
    left = 0
    right = len(input) - 1
    while left <= right:
        input[left], input[right] = input[right], input[left]    
        left += 1
        right -= 1
    input = [i[::-1] for i in input]
    return input
    
print(reverse_rev(words))
print("\n")
print("Just list")
print(words)


# Exercise #2
# Create a function that counts how many distinct words are in the string below, 
# then outputs a dictionary with the words as the key and the value as 
# the amount of times that word appears in the string.
# Should output:
# {'a': 5,
# 'abstract': 1,
# 'an': 3,
# 'array': 2, ... etc...

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

def same_words(input):
    count_words = {}
    comma = list(input.split(","))
    a_list = "".join(comma)
    peroid = list(a_list.split("."))
    final_list = "".join(peroid).lower()
    final_list = list(final_list.split(" "))

    for word in final_list:
        if word in count_words.keys():
            count_words[word] += 1
        else:
            count_words[word] = 1
        

    return count_words

print(same_words(a_text))


# Exercise #3
# Write a program to implement a Linear Search Algorithm. 
# Also in a comment, write the Time Complexity of the following algorithm.

# Hint: Linear Searching will require searching a list for a given number.

num = [1,3,'5',7,"a",2,"4",6,9,8]

def linear_search(input, k):
    for i in range(len(input)):
        try:
            if int(input[i]) == k:
                return input[i]
        except:
            continue
    return False

print(linear_search(num, 4))

