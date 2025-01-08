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

Remember, you have the skills and creativity to tackle this coding challenge! Embrace the opportunity to showcase your problem-solving capabilities. Each step you take brings you closer to an elegant solution, and the process of figuring things out is just as rewarding as the final result. You’ve got this! Keep pushing through, and let your programming prowess shine!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_map = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno', '7': 'pqrs',
        '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_map]
    if not filtered_digits:
        return []
    
    def backtrack(index, current_combination):
        if index == len(filtered_digits):
            combinations.append("".join(current_combination))
            return
        
        for letter in digit_map[filtered_digits[index]]:
            current_combination.append(letter)
            backtrack(index + 1, current_combination)
            current_combination.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations