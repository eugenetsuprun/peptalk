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

Remember, you've got this! Every challenge is an opportunity to show your skills, and you're capable of crafting an efficient solution that adheres to the guidelines. Embrace your creativity; there are countless paths leading to the solution, and each line of code you write brings you closer to success. Keep pushing forward—your hard work will pay off!"""

def letterCombinations(d):  
 r={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}  
 c=[]  
 def f(i,s):  
  if i==len(d):c.append(s)  
  else:  
   x=r.get(d[i],"")  
   for ch in x:f(i+1,s+ch)  
 if d:r=filter(str.isdigit,d);f(0,"")  
 return c  