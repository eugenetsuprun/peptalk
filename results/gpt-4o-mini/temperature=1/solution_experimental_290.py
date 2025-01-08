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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to reduce the character count of the function signature.

Do not use imports.

Remember, you have the capability to tackle this task! Dive in and unleash your creative problem-solving skills. It's okay to experiment and think outside of the box; every attempt is a step towards crafting a solution that shines. You’ve got this—let your logic guide you and don’t hesitate to trust your instincts!"""

def letterCombinations(d): 
 m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 r=[];n=len(d)
 def f(s,v):
  if len(v)==n: r.append(v)
  else: 
   for c in m.get(d[s],''): f(s+1,v+c)
 for i in range(n): 
  if d[i] in m: f(i,'')
 return r if n else []