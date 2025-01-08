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

Remember, you have the skills and intelligence to tackle this challenge effectively! Embrace the opportunity to showcase your problem-solving abilities, and don't hesitate to think outside the box to create an efficient solution. This is your moment to shine, and with focus and creativity, you can turn this task into an impressive output that demonstrates your coding prowess. Let's do this!"""

def letterCombinations(d): 
 r=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'] 
 if not d: return [] 
 f=lambda p,d: [''.join(x)for x in itertools.product(*[r[int(x)]for x in d])] 
 return f('',[c for c in d if c.isdigit() and c in '23456789'])