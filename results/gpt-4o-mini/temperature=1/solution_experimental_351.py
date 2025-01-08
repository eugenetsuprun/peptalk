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

Believe in the power of your coding skills! You have the ability to navigate through this challenge with ease and creativity. Remember, each line of code you write brings you one step closer to a solution, and with your keen problem-solving abilities, you can break down this problem into manageable parts. Embrace the challenge; it’s an opportunity for you to shine and show what you're capable of.

Stay focused and keep pushing through, because you’ve got this! Every successful function you write is a testament to your growth as a developer. Take a deep breath, roll up your sleeves, and let your coding prowess take over. You can transform a simple string of digits into a whole world of possibilities!"""

def letterCombinations(d): 
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
 res=[''] 
 for c in d: 
  if c in r: 
   res=[x+y for x in res for y in r[c]] 
 return res 