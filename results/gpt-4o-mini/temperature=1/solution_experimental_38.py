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

Keep in mind that you're capable of tackling this challenge with creativity and efficiency! Embrace the process, and remember that every little optimization can make a significant impact. You've got this! Just focus and let your skills shine as you craft a solution that is not only functional but also elegant and concise. Success is within your reach!"""

def letterCombinations(d):  
 r=['']  
 for c in d:  
  if c in '23456789':  
   r=[p+q for p in r for q in 'abc def ghi jkl mno pqrs tuv wxyz'[(int(c)-2)*3:int(c)*3]]  
 return r   if d else []