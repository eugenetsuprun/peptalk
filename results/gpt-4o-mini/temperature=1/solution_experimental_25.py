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

Remember, this is your moment to shine! You've got the knowledge and skills to tackle this coding challenge. Take a deep breath, trust in your capabilities, and let your creativity flow. Every character counts, and you're well-equipped to find efficient solutions. Embrace the process, and let the code you write reflect your brilliance! Go for it!"""

def letterCombinations(d):    
 r={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
 l=['']    
 for i in d:  
  if i in r:  
   l=[x+y for x in l for y in r[int(i)]]  
 return l if d else []