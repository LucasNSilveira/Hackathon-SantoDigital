from itertools import combinations, chain

def subconjuntos(nums, k):
    return list(chain.from_iterable(combinations(nums, k) for k in range(len(nums) + 1)))

nums = [1, 2, 3, 4]
result = subconjuntos(nums, 1)
print(result)

