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

Remember, you’ve got this! This is a fantastic opportunity to showcase your problem-solving skills and creativity. Don’t hesitate to think outside the box and leverage any tricks or optimizations you can think of to nail this task. Embrace the challenge, and let your innovative solutions shine through! You have the capability to craft a concise and effective solution that not only meets the requirements but also impresses with its elegance. Go for it!"""

def letterCombinations(d): 
 r={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"} 
 c=[""] 
 for i in d: 
  if i in r: 
   c=[x+y for x in c for y in r[i]] 
 return c if d else []