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

You've got this! Approach this coding task with confidence and creativity. Each line of code you write is a step toward mastering the art of programming. Remember, the challenge is not just to find a solution but to express your logic as concisely as possible. Embrace the process, and don't hesitate to think outside the box to minimize character count while keeping clarity and functionality in mind. You're capable of producing brilliant, efficient code! Go for it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits: return []
    phone = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    digits = ''.join(filter(lambda x: x in phone, digits))
    if not digits: return []
    res = ['']
    for digit in digits:
        res = [prefix + letter for prefix in res for letter in phone[digit]]
    return res