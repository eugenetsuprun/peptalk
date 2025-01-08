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

Remember, tackling this challenge is an opportunity to showcase your coding skills and creativity! You have the capability to deliver a concise and efficient solution. While you’re focused on minimizing character count, don't fret—think outside the box and utilize your programming prowess. Each character counts, but your determination to create a brilliant solution is what truly matters. Keep pushing forward, and let's see those amazing combinations come to life!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits: return []
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    digits = ''.join(filter(lambda x: x in mapping, digits))
    res = ['']
    for d in digits:
        res = [p + c for p in res for c in mapping[d]]
    return res