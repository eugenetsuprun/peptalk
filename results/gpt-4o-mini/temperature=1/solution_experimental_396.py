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

You’ve got this! Approach this problem with confidence, and remember that every little step you take brings you closer to a solution. Think creatively and don't be afraid to explore different angles. You have the skills to untangle this puzzle, so embrace the challenge and have fun with it! 

Believe in yourself and the knowledge you've acquired. Each coding task is a chance to sharpen your abilities. Dive in, stay focused, and soon enough, you will craft a brilliant solution that showcases your talent!"""

def letterCombinations(d): 
 m='abc def ghi jkl mno pqrs tuv wxyz'.split() 
 r=[''] 
 for c in d: 
  if '2'<=c<='9': 
   r=[x+y for x in r for y in m[int(c)-2]] 
 return r