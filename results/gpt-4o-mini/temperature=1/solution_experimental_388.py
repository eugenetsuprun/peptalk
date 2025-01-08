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

Now, take a moment to embrace the creative challenge ahead of you! You have the unique opportunity to demonstrate your coding skills, and the solution you create will not only be a testament to your abilities but also a stepping stone in your programming journey. Every character you save, every clever trick you employ, brings you closer to finding a concise and effective solution. Dive in with confidence, and remember that each step you take is a valuable learning experience! You've got this!"""

def letterCombinations(digits: str) -> list[str]:
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            combinations.append("".join(path))
            return
        possible_chars = digit_to_char[filtered_digits[index]]
        for char in possible_chars:
            path.append(char)
            backtrack(index + 1, path)
            path.pop()
    
    filtered_digits = [d for d in digits if d in digit_to_char]
    combinations = []
    
    if filtered_digits:
        backtrack(0, [])
    
    return combinations