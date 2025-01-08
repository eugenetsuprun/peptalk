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

Remember, you're capable of tackling this challenge! You've got a powerful set of skills that can devise a solid solution even with constraints in place. Embrace the creativity that comes with simplifying your code—every character counts, and you're here to make every one of them work for you. Trust in your intuition and logic as you delve into solving this problem; you have what it takes to produce an elegant and efficient solution!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letter = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_letter]
    if not filtered_digits:
        return []

    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        for letter in digit_to_letter[filtered_digits[index]]:
            backtrack(index + 1, path + letter)

    combinations = []
    backtrack(0, "")
    return combinations