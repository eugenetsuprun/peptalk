"""Given a string of digits from 2 through 9, return all possible letter combinations that the number could represent (in any order).

Mapping of digits to letters:

Button 2: ABC  
Button 3: DEF  
Button 4: GHI  
Button 5: JKL  
Button 6: MNO  
Button 7: PQRS  
Button 8: TUV  
Button 9: WXYZ  

The number might have some non-digit characters, ones, or zeros. Filter them out.

Example 1:

Input: digits = "23"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:  
Input: digits = ""  
Output: []

Example 3:  
Input: digits = "2"  
Output: ["a","b","c"]

Example 4:  
Input: digits = "12*30"  
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

The length of digits will be between 0 and 4.  
digits[i] is a digit in the range ['2', '9'].

The function signature is: letterCombinations(digits: str) -> list[str]

Remember, you have the capability to create an elegant solution that combines brevity with clarity. Embrace the challenge of coding and let your creativity flow! Every character saved is a testament to your ingenuity, so think outside the box and trust in your ability to deliver a concise yet effective function. You've got this! Now, go ahead and craft that solution!"""

```python
def letterCombinations(digits: str) -> list[str]:
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    def backtrack(i, path):
        if i == len(filtered_digits):
            combinations.append(path)
            return
        for letter in phone[filtered_digits[i]]:
            backtrack(i + 1, path + letter)
    
    filtered_digits = [d for d in digits if d in phone]
    combinations = []
    if filtered_digits:
        backtrack(0, "")
    return combinations
```