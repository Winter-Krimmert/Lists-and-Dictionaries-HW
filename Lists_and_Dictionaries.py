# Advanced Operations on Python Lists

# 1.

def squares_list(n):
    return [i**2 for i in range(1, n+1)]

print(squares_list(5))
# Time Complexity - O(n) - iterating through numbers 1 to n. This is a linear time operation.
#  Space Complexity - O(n) - storing n squares in the list. This is a linear space operation.

# 2.

def reverse_sublist(arr, i, j):
    arr[i:j+1] = arr[i:j+1][::-1]
    return arr
arr = [1, 2, 3, 4, 5]
print(reverse_sublist(arr, 1, 3))
#  Time Complexity - O(j-i) - reversing the sublist from index i to j. This is a constant time operation.
#  Space Complexity - O(1) - no additional space used. This is a constant space operation.

# 3.

def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    merged.extend(list1[i:])
    merged.extend(list2[j:])

    return merged 

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))
# Time Complexity - O(len(list1) + len(list2)) - iterating through both lists once. This is a linear time operation.
# Space Complexity - O(len(list1) + len(list2)) - storing all elements in the merged list. This is a linear space operation.



# Dictionary Manipulation and Optimization

# 1. 

def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy() # make a copy of dict1 
    merged_dict.update(dict2) # update the copy with dict2. preseving the original dict2 keys.
    return merged_dict




dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(merge_dicts(dict1, dict2))

# time complexity - O(n) for n number of keys in dict1 that we're iterating through. iterating through dict2 and merging in merge_dict is O(m) for m number of keys in dict2. Overall time complexity is O(n + m).

# Space Complexity - copy of dict1: O(n) because a dictionary of the same size as 'dict1' is created. O(n) - storing n keys in the merged_dict. This is a linear space operation if all keys are unique. Overall space complexity - O(n+m).

2.

def dict_difference(dict1, dict2):
    result = {}

    for key in dict1:
        if key not in dict2:
            result[key] = dict1[key]

    for key in dict2:
        if key not in dict1:
            result[key] = dict2[key]

    return result

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
print(dict_difference(dict1, dict2))

# Time Complexity - iterating over dict1 O(n) where n is the number of elements in 'dict1'. Iterating over dict2 O(m) where m is the number of elements in 'dict2'. Key lookups O(1) Overall time complexity is O(n + m). Linear.

# Space Complexity - O(n + m) - storing all keys that are unique to either dict1 or dict2. This is a linear space operation.



3.

def count_word_frequency(word_list):
    word_count = {}

    for word in word_list:
        word = word.lower() # Convert to lowercase to ignore case
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

# Example usage
words = ["Apple", "Banana", "apple", "Orange", "banana", "orange", "APPLE"]
print(count_word_frequency(words))

# Time complexity - O(n) - Iterating through the list O(n), coverting each word to lowercase O(k) where k is the length of the word. Checking and updating the dictionary O(1). Overall time complexity is O(n*k) where n is the number of words and k is the average length of the words.
# Space Complexity - O(m), where m is the number of unique words in the list. Storing the frequency of each unique word. This is a linear space operation.