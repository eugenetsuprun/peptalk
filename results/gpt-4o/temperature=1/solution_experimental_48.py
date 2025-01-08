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

Now, let's tackle this challenge with confidence! This problem is a great opportunity to showcase your coding skills and creativity. You'll be synthesizing combinations and filtering inputs in a way that not only enhances your problem-solving abilities but also reinforces your grasp of string manipulation. Remember, every line of code you write is a step toward mastery. Embrace the journey, and know that you have the capability to produce an efficient and elegant solution. Keep pushing the boundaries of what's possible!"""

```python
def letterCombinations(digits: str) -> list[str]:
    d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    r, C = [''], c.__getitem__
    for n in filter(lambda x: x in d, digits):
        r = [p + c(d[n],i) for p in r for i in range(len(d[n]))]
    return r if digits else []
```