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

Remember, you've got this! You're equipped with the knowledge and skills honed through extensive training. Embrace the challenge of this coding task; every problem you solve is a stepping stone toward mastery. Let your creativity shine as you explore efficient solutions, and don’t hesitate to think outside the box. You’re on the right path to not just find a solution but to excel in crafting one that is both functional and elegant. Keep pushing forward, and let the code flow!"""

def letterCombinations(d): 
 r=[''] if d else []; 
 m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}; 
 for x in d: 
  if x in m: 
   r=[p+q for p in r for q in m[x]]; 
 return r