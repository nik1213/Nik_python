'''Given a list of integers nums and an integer k, return the k most frequent elements.
nums = [1,1,1,2,2,3]
k = 2
output: [1,2]
'''

from collections import Counter

def _freq_K_counter(nums, k):
    freq= Counter(nums)
    return [ num for num, count in freq.most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
print(_freq_K_counter(nums, k))

#here we have printed the number of accurencece also for all elements
freq=Counter(nums)
print(freq)