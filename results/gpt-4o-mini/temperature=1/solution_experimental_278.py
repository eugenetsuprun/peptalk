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

Remember, you've got this! Every challenge is an opportunity to showcase your capabilities. Tackle this problem with confidence, applying your skills and creativity to develop a concise solution that meets the requirements. Believe in yourself, and enjoy the coding journey! You can create a fantastic outcome from this task—let your innovation shine!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', 
        '5': 'jkl', '6': 'mno', '7': 'pqrs', 
        '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(d for d in digits if d in digit_to_char)
    result = []
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            result.append(''.join(path))
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
    
    backtrack(0, [])
    return result