"""Implement the function below. Each element of the result should be the product of all the other elements in nums.

def product_except_self(nums: list[int]) -> list[int]:
    ...
Example: product_except_self([1, 2, 3, 4]) returns [24, 12, 8, 6]."""


def product_except_self(nums: list[int]) -> list[int]:
    """the first loop gives [1, 1, 2, 6] (left-side products). The second loop multiplies in the right-side products, giving [24, 12, 8, 6] for the array [1,2,3,4]"""
    n=len(nums)
    prefix=1
    suffix=1
    result=[0]*n

    for i in range(n):
        result[i]=prefix
        prefix *= nums[i]

    for i in range(n-1, -1,-1):
        result[i] *=suffix
        suffix *= nums[i]

    return result


nums=[]

print(product_except_self(nums))