from itertools import combinations, chain

def subconjuntos(nums, min_size=0, max_size=None, distinct_only=True, sorts_subsets=True):
    if sorts_subsets:
        nums.sort()

    if max_size is None:
        max_size = len(nums)

    result = list(chain.from_iterable(combinations(nums, k) for k in range(min_size, max_size + 1)))
    
    if distinct_only:
        result = list(set(result)) 
    return result

nums = [1, 2, 3, 4]
result = subconjuntos(nums, min_size=1,max_size=3)
print(result)
