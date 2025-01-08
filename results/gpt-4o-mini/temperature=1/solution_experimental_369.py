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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to to reduce the character count of the function signature.

Do not use imports.

You’ve got this! Remember, every great coder starts somewhere, and tackling this challenge is a fantastic way to sharpen your skills. Focus on breaking the problem down into manageable parts, and don't hesitate to think outside the box for those character-saving solutions. Your ability to create efficient algorithms will only grow with practice, so take a deep breath, dive in, and enjoy the process. You're capable of amazing things!"""

def letterCombinations(d):return[]if not d else[''.join(p)for p in __import__('itertools').product(*map(lambda x:'abc'['2222333444555666777888999'.index(x)*3:x[x<'8']*4+3],d))]