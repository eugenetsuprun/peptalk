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

You've got this! Remember, the key to solving this problem lies in breaking it down into manageable parts. Think about how you can leverage recursion or backtracking to generate the combinations effectively. Embrace your coding skills and creativity! Every line you write brings you closer to the solution, and you're more than capable of crafting a concise and elegant implementation. Keep pushing forward, and trust in your ability to solve this challenge!"""

def letterCombinations(d):  
 m={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}  
 res=[]  
 def backtrack(path,i):  
  if i==len(d):res.append(path)  
  else:  
   for c in m.get(d[i],''):  
    backtrack(path+c,i+1)  
   return  
 if d:backtrack('',0)  
 return res  

letterCombinations('12*30')  