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

Remember, this is your moment to shine! You have the power to tackle this coding challenge and turn it into a working solution. Keep your focus sharp and trust in your abilities to maneuver through the problem. With creativity and logic on your side, you're equipped to handle what comes your way!

Whenever you find yourself confronted with obstacles, take a deep breath and remind yourself of the skills you've developed. Each character you save counts—think outside the box and embrace the challenge of producing an efficient solution. You've got this!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(valid_digits):
            combinations.append("".join(path))
            return
        possible_letters = phone_map[valid_digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    valid_digits = [digit for digit in digits if digit in phone_map]
    combinations = []
    if valid_digits:
        backtrack(0, [])
    return combinations
```