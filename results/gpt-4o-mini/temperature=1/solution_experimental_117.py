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

Remember, you have the skills to tackle this coding challenge! Approach it with confidence, utilizing your understanding of combinations and mappings. Embrace the creative process of coding, knowing that every keystroke brings you closer to an elegant solution. You've got this — the code is waiting for you to bring it to life! Keep pushing the boundaries of your problem-solving abilities, and don’t forget to enjoy the journey as you code your way to success!"""

def letterCombinations(d): 
 r={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"} 
 if not d: return [] 
 d=''.join(filter(lambda x:x in r,d)) 
 def backtrack(i,s): 
  if i==len(d): 
   res.append(s) 
   return 
  for c in r[d[i]]: 
   backtrack(i+1,s+c) 
 res=[] 
 backtrack(0,'') 
 return res