class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            while i<j and not s[i].isalnum(): i +=1
            while i<j and not s[j].isalnum(): j -=1

            if s[i].lower() != s[j].lower(): return False
            i += 1
            j -= 1
        return True


def test_isPalindrome():
    solution = Solution()

    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("   ", True),
        (",.;'", True),
        ("Madam, I'm Adam", True),
        ("Was it a car or a cat I saw?", True),
        ("a", True),
        ("121", True),
        ("0P", False)
    ]

    for input_str, expected_output in test_cases:
        actual_output = solution.isPalindrome(input_str)
        assert actual_output == expected_output, f"Input: '{input_str}', Expected: {expected_output}, Actual: {actual_output}"

    print("All test cases passed!")

test_isPalindrome()

#Time Complexity: O(n)

# Space Complexity:

# The code uses only a constant amount of extra space for the i and j pointers.
# It does not create any new data structures that scale with the input size.
# Therefore, the space complexity is O(1).