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

You’ve got this! Remember that every bit of effort you put into this coding challenge is a step toward mastering the art of problem-solving. The task at hand is a great opportunity to flex your coding muscles and enhance your ability to think critically. Embrace the challenge, and know that you have the skills and creativity to turn that string of digits into beautiful combinations of letters. Now, dive in and showcase your coding prowess!

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to to reduce the character count of the function signature.

Do not use imports."""

def letterCombinations(d): 
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 if not d: return []
 d=[r[x] for x in d if x in r]
 def f(p,s):
  if not s: return [p]
  return f(p+s[0],s[1:]) + f(p,s[1:])
 return f('',d[0]) if len(d)==1 else f('',d[0]) if len(d)==2 else f('',d[0]) if len(d)==3 else f('',d[0]) if len(d)==4 else []