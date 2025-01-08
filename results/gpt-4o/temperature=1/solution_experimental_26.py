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

It's time to dive deep into this challenge, and remember that coding is not just about getting the solution—it's about enjoying the journey of problem-solving! Look at this task as an exciting puzzle. Each step you take will bring you closer to fully cracking it. Trust in your skills, embrace any challenges, and let your creativity shine as you find ways to streamline and optimize your solution. You’ve got this!

Now, focus on breaking down the problem logically and creatively. Don't hesitate to experiment with different strategies. Remember, every attempt—successful or not—brings you learning and growth. Let the thrill of coding guide you through this task!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if len(digits) == 0: return []
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = ['']
    for d in digits:
        if d in mapping:
            res = [p + l for p in res for l in mapping[d]]
    return res
```