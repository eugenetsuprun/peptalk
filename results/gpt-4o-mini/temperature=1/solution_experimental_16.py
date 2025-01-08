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

You got this! Remember, every coding challenge is a chance to learn and showcase your skills. Embrace the process and don't shy away from exploring different approaches. Trust in your ability to find clever solutions, and have fun with the problem-solving journey! Your creativity and resilience will shine through as you tackle this task. Go for it, and let your coding prowess rise to the occasion!"""

def letterCombinations(digits: str) -> list[str]:
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
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        letters = digit_to_letters[filtered_digits[index]]
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    filtered_digits = [d for d in digits if d in digit_to_letters]
    combinations = []
    
    if filtered_digits:
        backtrack(0, "")
        
    return combinations