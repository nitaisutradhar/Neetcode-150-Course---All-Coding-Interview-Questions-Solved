class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))
    

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

# Time Complexity: O(n)
# Space Complexity: O(n)