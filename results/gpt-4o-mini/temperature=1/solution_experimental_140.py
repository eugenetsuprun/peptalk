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

You've got this! Remember, every coding challenge is an opportunity to learn and grow. Don’t be afraid to experiment and get creative with your solutions. Every line of code you write is a step towards mastering your skills. Embrace the process, trust your abilities, and know that you've got the tools to tackle this problem head-on! Keep pushing forward, and you'll be amazed at what you can achieve."""

def letterCombinations(d): 
 r=[''] if d else[]; 
 for x in d: 
  if x in'23456789': 
   r=[p+c for p in r for c in' abcdefghijklmnopqrstuvwxyz'[ord(x)-50:ord(x)-47]]; 
 return[r[1:]]