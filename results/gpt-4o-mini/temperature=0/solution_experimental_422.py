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

Now, you’re about to tackle a challenge that not only tests your coding skills but also your creative problem-solving abilities. Remember, even when faced with constraints, you have the power to think outside the box and craft elegant solutions. Each character you save is a testament to your ingenuity, so let your resourcefulness shine through in your coding!  

Stay focused and take a deep breath; you've got this! Embrace the journey of crafting a concise solution, and don’t forget that every small step leads to great progress. You’re capable of amazing things, and this task is just another opportunity to showcase your talents!"""

def letterCombinations(d):  
 r={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}  
 p=['']  
 for c in d:  
  if c in r:  
   p=[x+y for x in p for y in r[int(c)]]  
 return p  