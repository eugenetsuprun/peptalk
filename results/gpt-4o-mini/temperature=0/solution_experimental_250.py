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

Remember, you’ve got this! Each line of code you write is a step towards a solution, and tackling this challenge is a fantastic way to showcase your skills. Embrace the process; it’s not just about getting to the end result, but enjoying the journey of problem-solving. Every little character counts, and your creativity in finding concise solutions will shine through. Let’s see how compactly you can express your brilliance!"""

def letterCombinations(digits: str) -> list[str]:
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    digits = ''.join(filter(lambda x: x in mapping, digits))
    if not digits:
        return []
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        for letter in mapping[digits[index]]:
            backtrack(index + 1, path + [letter])
    
    combinations = []
    backtrack(0, [])
    return combinations