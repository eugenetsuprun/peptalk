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

You've got this! Remember, every great coder starts with a challenge, and this is your moment to shine. Think of this task as a puzzle waiting to be solved. Each combination you generate will come together like pieces of a beautiful mosaic. Trust in your abilities and let your creativity flow! Embrace the process, and remember that every step, no matter how small, brings you closer to a fantastic solution. Keep pushing forward!"""

def letterCombinations(d): 
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
 c=[] 
 def f(s,i): 
  if i==len(s): 
   c.append('') 
   return 
  for j in r.get(s[i],''): 
   f(s,i+1) 
   for k in c[:-1]: 
    c.append(k+j) 
   c.pop() 
 f(''.join(filter(str.isdigit,d)),0) 
 return c[1:] 