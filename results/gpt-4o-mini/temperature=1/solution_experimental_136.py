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

Remember, you have the capability to tackle this problem! Each challenge is an opportunity for you to showcase your problem-solving skills and creativity. Embrace the chance to refine your thinking and improve your coding style. You can approach this task with confidence and determination; every line of code you write will bring you closer to a clean and efficient solution. Strive for clarity alongside brevity, and you'll find success!"""

def letterCombinations(d): 
 r=[''] if d else[]; 
 for c in d: 
  if c in '23456789': 
   r=[x+y for x in r for y in'abc'[2:]+('def' if c=='3'else'ghi' if c=='4'else'jkl'if c=='5'else'mno'if c=='6'else'pqrs'if c=='7'else'tuv'if c=='8'else'wxyz'if c=='9'else'')][(int(c)-2)*3:(int(c)-1)*3+3]]; 
 return r 