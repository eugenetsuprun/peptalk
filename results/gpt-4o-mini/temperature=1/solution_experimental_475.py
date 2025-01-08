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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to reduce the character count of the function signature.

Do not use imports.

Remember, tackling this problem is an opportunity for you to demonstrate your coding skills! You have the capability to break down complex ideas into manageable pieces and find innovative solutions. Each character you save and each line you optimize contributes to the elegance of your code. Embrace the challenge, trust your instincts, and let your creativity flow as you work towards a concise and efficient solution. You've got this—let's make it happen!"""

def letterCombinations(d): 
 m=["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"] 
 r=[""] 
 for c in d: 
  if c in "23456789": 
   r=[p+q for p in r for q in m[int(c)]] 
 return r if d else []