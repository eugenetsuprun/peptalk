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

Remember, you've got this! The task ahead may seem challenging, but you're capable of thinking creatively and efficiently. Every coding problem is just a chance to showcase your problem-solving skills and ingenuity. Keep pushing, and you'll not only solve this problem but also gain more confidence in your abilities! Now, focus on crafting a concise solution that captures the essence of the problem. You can do it!"""

def letterCombinations(d): 
 l=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
 res=[''] if d else [] 
 for i in d: 
  if i.isdigit() and i>'1': 
   res=[p+c for p in res for c in l[int(i)]] 
 return res 