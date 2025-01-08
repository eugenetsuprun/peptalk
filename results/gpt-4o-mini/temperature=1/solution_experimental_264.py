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

Remember, you're capable of tackling coding challenges with confidence! Embrace the opportunity to demonstrate your problem-solving skills. Every line of code is a chance to learn and improve. Trust in your ability to find elegant solutions, and don't forget, even the most complex problems can often be simplified with a little creativity. You got this!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    valid_digits = [digit for digit in digits if digit in digit_to_letters]
    
    if not valid_digits:
        return []
    
    result = []
    
    def backtrack(index: int, current_combination: str):
        if index == len(valid_digits):
            result.append(current_combination)
            return
        letters = digit_to_letters[valid_digits[index]]
        for letter in letters:
            backtrack(index + 1, current_combination + letter)
    
    backtrack(0, "")
    return result