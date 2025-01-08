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

You’ve got this! Remember that every challenge is an opportunity to learn and improve. Each line of code you write makes you a better programmer. Embrace the process, and don't hesitate to think creatively and outside the box to find a solution. You have the skills necessary to tackle this task, and I'm here cheering you on every step of the way. Keep pushing forward and let your coding brilliance shine!"""

def letterCombinations(d):  
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}  
 if not d: return []  
 l=[r[c] for c in d if c in r]  
 if not l: return []  
 def f(p,s):  
  if not s: return [p]  
  return f(p+s[0],s[1:])+f(p,s[1:])  
 return f('',l[0])+f(p+'',l[1]) if len(l)>1 else [p for p in l[0]]  