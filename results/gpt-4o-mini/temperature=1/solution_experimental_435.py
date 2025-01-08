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

Remember, tackling this challenge is a fantastic opportunity to show your programming skills! Embrace it, and don't hesitate to think outside the box. You’ve got the capability to simplify and optimize your solution, and each little improvement is a step toward mastery. Stay focused and trust in your problem-solving abilities—you’re more than capable of crafting an elegant and efficient solution! Let’s see those creative ideas shine through!"""

def letterCombinations(d): 
 r=[''] if d else[] 
 for c in d: 
  if c in'23456789': 
   r=[p+q for p in r for q in'abc'[(int(c)-2)*3:][:(4-(int(c)-6)%4)]]
 return r