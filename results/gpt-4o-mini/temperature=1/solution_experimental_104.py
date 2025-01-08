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

Remember, you have the capability to break the problem down into manageable pieces. Take a deep breath and approach this task confidently—you’ve got the skills to tackle it effectively. Each line of code you write can be a stepping stone toward a clear solution, and with focus, you can minimize the character count without sacrificing functionality. Trust in your ability to optimize and create a solution that not only works but shines!"""

def letterCombinations(d):  
 r=["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]  
 p=[""]  
 for i in d:  
  if i>'1' and i<'a':  
   p=[x+y for x in p for y in r[int(i)]]  
 return p