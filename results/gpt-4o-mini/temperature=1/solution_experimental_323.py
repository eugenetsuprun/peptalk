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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to in order to reduce the character count of the function signature.

You’ve got this! Trust in your capabilities to dissect this challenge and deliver a solution that’s not only effective but also concise. Coding is as much an art as it is a science, and with your skills, you're bound to create something impressive. Remember, every great coder started just like you—facing challenges and learning from each one. Embrace the process and let your creativity shine through in your solution!"""

def letterCombinations(d): 
 m={ '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz' }
 p=[''] if d else []
 for x in d:
  if x in m:
   p=[a+b for a in p for b in m[x]]
 return p