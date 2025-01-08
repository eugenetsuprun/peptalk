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

Believe in your ability to tackle this challenge. You have the skills needed to creatively navigate through the complexities of this problem and produce an efficient solution. Remember, every step you take brings you closer to your goal. You can think outside the box and find ways to simplify without compromising the solution's integrity. Go ahead and give it your best shot!"""

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    # Mapping of digits to corresponding letters
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Filter out invalid characters
    digits = ''.join(filter(lambda d: d in digit_to_letters, digits))

    if not digits:
        return []

    # Helper function to generate combinations
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return

        possible_letters = digit_to_letters[digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations
```