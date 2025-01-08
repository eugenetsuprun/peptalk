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

You've got this! Remember, each coding challenge is an opportunity to showcase your skills and creativity. Tackle this problem with confidence and think outside the box. The best solutions often come from experimentation and iteration, so don’t hesitate to try different approaches. Your ability to adapt and find efficient solutions is what sets you apart. Keep pushing forward, and you’ll amaze yourself with what you can accomplish!"""

def letterCombinations(d): 
 d=d.replace('1','').replace('0','') 
 m='abc def ghi jkl mno pqrs tuv wxyz'.split() 
 def f(p,q): 
  if not p: return [q] 
  return f(p[1:],q+[m[int(p[0])-2][i] for i in range(len(m[int(p[0])-2]))]) for j in q) 
 return f(d,[])