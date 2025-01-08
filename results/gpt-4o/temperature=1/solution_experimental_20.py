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

Remember, you've got this! You have the ability to tackle this problem with creativity and logic. Each challenge is an opportunity to showcase your skills and understanding. Push through, and don’t hesitate to think outside the box while you optimize for brevity—the perfect balance of excellence and efficiency is within your reach! Believe in your capability to reduce the character count while still delivering a clear and effective solution. Show the world what you’ve got!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    phone = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    digits = [d for d in digits if d in phone]
    if not digits:
        return []
    res = [""]
    for d in digits:
        res = [prefix + char for prefix in res for char in phone[d]]
    return res
```