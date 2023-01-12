from tqdm import tqdm

def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    Solving Leetcode Problem.
    https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
    
    Given two positive integers startPos and endPos
    Initially, you are standing at position startPos on an infinite
    number line. With one step, you can move either one position to the left,
    or one position to the right.
    
    Given a positive integer k, return the number of different ways to
    reach the position endPos starting from startPos, such that you
    perform exactly k steps.
    """
    #@cache
    def dfs(s, left):
        if left == 0:
            if s == endPos:
                return 1
            return 0
        return (dfs(s - 1, left-1) + dfs(s+1, left-1))%(10**9+7)
    return dfs(startPos, k)%(10**9+7)


def test_number_of_ways():
    """
    Example 1:

    Input: startPos = 1, endPos = 2, k = 3
    Output: 3
    Explanation: We can reach position 2 from 1 in exactly 3 steps
    in three ways:
    - 1 -> 2 -> 3 -> 2.
    - 1 -> 2 -> 1 -> 2.
    - 1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.
    """
    print(numberOfWays(1, 2, 3))

if __name__ == "__main__":
    test_number_of_ways()
