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

---

You're embarking on a coding challenge that allows you to showcase your inventive problem-solving skills! Remember, every great coder started somewhere, and this is your opportunity to shine. Trust in your capabilities—you have the tools to create a solution that's both efficient and elegant. 

Stay focused, break the problem down, and delight in the process of programming. Each step you take gets you closer to a well-crafted solution. You can do this! Let your creativity and logic flow as you tackle the task ahead."""

def letterCombinations(d):
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 if not d: return []
 d=''.join(filter(lambda x:x in r,d))
 def f(p,d): 
  if not d: return [p]
  return f(p+d[0],d[1:]) + f(p+d[1],d[2:])
 return f('',r[d[0]])+f('',r[d[1]])+f('',r[d[2]])+f('',r[d[3]]) if len(d)<5 else []