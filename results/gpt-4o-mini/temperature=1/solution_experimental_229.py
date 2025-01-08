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

---

You're on the brink of tackling a fun and engaging challenge that combines logic and creativity. Remember, coding is about problem-solving, and every line you write is a step toward discovering an elegant solution. Trust your instincts and let your code reflect your unique problem-solving style. This is a chance to shine, so embrace it and enjoy the process!

You have the skills needed to find a solution that not only works efficiently but also showcases your ability to think outside the box. Keep pushing forward, and don't hesitate to experiment! Every attempt is a learning experience, and you're capable of producing something incredible. Let’s see what you can create!"""

def letterCombinations(d): 
 m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
 p=[''] if d else [] 
 for c in d: 
  if c in m: 
   p=[x+y for x in p for y in m[c]] 
 return p