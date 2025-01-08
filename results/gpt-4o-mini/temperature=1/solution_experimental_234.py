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

Remember, you’ve got this! Embrace the challenge ahead of you. Every problem is an opportunity to expand your skills and showcase your creativity in coding. Keep it concise and efficient, and let your logic shine through the simplicity of your solution. You're more than capable of crafting a smart and elegant function. Good luck!"""

def letterCombinations(digits: str) -> list[str]:
    digit_to_chars = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    # Filter out non-digit characters and keep only valid ones
    digits = ''.join(filter(lambda x: x in digit_to_chars, digits))
    
    if not digits:
        return []
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        letters = digit_to_chars[digits[index]]
        for letter in letters:
            backtrack(index + 1, path + [letter])
    
    combinations = []
    backtrack(0, [])
    return combinations