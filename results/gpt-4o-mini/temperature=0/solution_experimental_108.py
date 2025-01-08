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

Remember, you’ve got this! Take a moment to visualize the solution unfolding as you work through the combinations. Each step brings you closer to a smart and efficient function, and you have the skills to make it happen. Embrace the challenge with confidence, and let your creativity shine through as you find the optimal way to express this solution in code. Keep pushing forward—you’re doing great!"""

def letterCombinations(d): 
 r={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'} 
 def f(s): 
  if not s: return [''] 
  return [x+y for x in r[int(s[0])] for y in f(s[1:])] 
 return f(''.join(filter(str.isdigit,d))) 