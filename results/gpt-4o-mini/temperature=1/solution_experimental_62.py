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

Now, remember that coding challenges are great opportunities for you to stretch your problem-solving muscles! This is your chance to demonstrate your creativity and efficiency in coding. You are capable of producing a concise and effective solution, so embrace the challenge! Take a deep breath, focus on breaking down the problem, and trust in your abilities to tackle this task with confidence and clarity. You’ve got this!"""

def letterCombinations(d): 
 r=["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]; 
 def p(d,s): 
  if not d: return [s] 
  return p(d[1:],c+s) for c in r[int(d[0])-2] 
 return p(''.join(filter(str.isdigit,d)),"") 