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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to to reduce the character count of the function signature.

Do not use imports.

You’ve got this! Tackling coding challenges can be tricky, but remember that you’re equipped with the knowledge and skills to find a solution. Take a moment to breathe and visualize breaking down the problem step by step. Each small win you achieve will add up to your final goal. Embrace the challenge, and let your creativity shine as you craft your solution!

Believe in yourself and your ability to solve this! Every programmer faces hurdles, but it's how you approach them that counts. Dive into the problem with confidence, and remember that persistence is key. You're capable of producing a fantastic solution, so let's get started and show what you can do!"""

```python
def letterCombinations(digits: str) -> list[str]:
    m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    r = [''] if digits else []
    for d in digits:
        if d in m:
            r = [p + q for p in r for q in m[d]]
    return r
```