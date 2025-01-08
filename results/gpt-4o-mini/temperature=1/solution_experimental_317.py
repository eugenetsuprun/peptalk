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

You're about to tackle a fun coding challenge that will stretch your abilities and sharpen your problem-solving skills! Embrace the task with confidence; remember that coding is not just about finding the right answer, but also about the journey of exploration and learning. Each line of code you write brings you closer to mastering the art of programming.

Stay focused and don't hesitate to think outside the box. There are always multiple ways to approach a problem, and your creativity can lead to elegant and efficient solutions. You've got the skills to tackle this, so dive in and show what you can do!"""

def letterCombinations(d): 
 r=[""] 
 m={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"} 
 for c in d: 
  if c in m: 
   r=[x+y for x in r for y in m[c]] 
 return r  if d else []