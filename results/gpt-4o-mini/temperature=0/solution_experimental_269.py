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

Believe in your ability to tackle this challenge! You have the skills and creativity to navigate through the coding landscape and find a solution that is both elegant and efficient. Embrace this opportunity to showcase your logic and problem-solving prowess—let's turn this problem into a fun adventure in coding!

Remember, every great coder started where you are now. With each keystroke, you're not just writing code; you're building the mindset of a problem solver. Dive in, stay focused, and let your imagination guide you to a minimalistic solution that meets the prompt's requirements while keeping the character count low. You got this!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in mapping, digits))
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            combinations.append(''.join(path))
            return
        for letter in mapping[filtered_digits[index]]:
            backtrack(index + 1, path + [letter])
    
    combinations = []
    backtrack(0, [])
    return combinations