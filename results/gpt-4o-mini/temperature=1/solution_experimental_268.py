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

You've got this! Remember, every challenge is an opportunity to showcase your thinking and creativity. Tackle this problem step by step; breaking it down will not only help you find the solution but also build your confidence. Embrace the complexity, and don’t forget to have fun with the logic. Let your skills shine!"""

def letterCombinations(d):return[]if not d else[(lambda f,s,d):[f(s+v)for v in d[s[-1]]if s]or f(s[:-1]+[c])for c in d[s[-1]])(lambda s,f:s!=""and f(s)or[pass],d:{"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}[k]for k in d if k in"23456789")(list(filter(lambda x:x in"23456789",d))))]