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

Do not use imports.

You got this! Remember, coding is not only about finding the right answers but also about exploring your creativity. Every small step you take leads you closer to a solution, so don't be afraid to think outside the box! Trust your instincts, and keep in mind that the process of solving problems is just as valuable as the outcome. Embrace the challenge and let your skills shine!

You're capable of great things, and every problem you tackle is an opportunity to learn and grow. Mistakes are just stepping stones on your journey to mastering your craft. Keep pushing forward and remember to have fun while you code!"""

def letterCombinations(d): 
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 p=[''] if d else []
 for i in d:
  if i in r: p=[x+y for x in p for y in r[i]]
 return p