from typing import List

def find_subsets(ind: int, nums: List[int], ds: List[int], ans_list: List[List[int]]) -> None:
    """
    Recursively find all unique subsets of a given set.

    Args:
        ind (int): The current index within the 'nums' list.
        nums (List[int]): The sorted input list of numbers.
        ds (List[int]): The current subset being generated.
        ans_list (List[List[int]]): A list to store the generated subsets.

    Returns:
        None

    Example:
        >>> ans = []
        >>> find_subsets(0, [1, 2, 2], [], ans)
        >>> ans
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    """
    ans_list.append(list(ds))
    for i in range(ind, len(nums)):
        if i != ind and nums[i] == nums[i - 1]:
            continue

        ds.append(nums[i])
        find_subsets(i + 1, nums, ds, ans_list)
        ds.pop()

def all_subsets(arr: List[int]) -> List[List[int]]:
    """
    Find all unique subsets of a given set.

    Args:
        arr (List[int]): The input set from which subsets are generated.

    Returns:
        List[List[int]]: A list of lists containing all unique subsets of the input set.

    Example:
        >>> all_subsets([1, 2, 2])
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    """
    nums = sorted(arr)
    ans_list: List[List[int]] = []
    find_subsets(0, nums, [], ans_list)
    return ans_list

if __name__ == "__main__":
    input_set = [10, 12, 12]
    subsets = all_subsets(input_set)

    for subset in subsets:
        print(subset, end=", ")
