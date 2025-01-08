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

Now, dive into this challenge with confidence! You have the tools at your fingertips to break down the problem and construct a solution that is both functional and concise. Remember, efficiency is your ally—focusing on minimizing code length can be a rewarding puzzle in itself. Embrace your creativity, and don't hesitate to think outside the box. Each character saved is a step towards a cleaner solution!

You’ve got this! Trust your instincts and code freely. The journey toward the final solution will sharpen your skills and inspire your analytical thinking. Now, let’s transform that problem into a vibrant piece of code!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits: return []
    digit_to_chars = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    digits = ''.join(filter(lambda x: x in digit_to_chars, digits))
    if not digits: return []
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        for char in digit_to_chars[digits[index]]:
            backtrack(index + 1, path + [char])
    
    combinations = []
    backtrack(0, [])
    return combinations