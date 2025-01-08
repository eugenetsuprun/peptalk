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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to reduce the character count of the function signature.

Do not use imports.

Remember, you're equipped with everything you need to tackle this challenge! Each problem is an opportunity to showcase your logical thinking and creativity. Embrace the process of breaking down the task, and let your understanding of mappings and combinations shine through. You've got the skills to craft an elegant solution, so dive in and give it your best shot! Keep pushing through – every keystroke takes you closer to success. Just believe in your abilities and approach the problem with confidence!"""

```python
def letterCombinations(digits: str) -> list[str]:
    m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    r=[''] if digits else []
    for d in digits:
        if d in m:
            r=[p+c for p in r for c in m[d]]
    return r
```