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

Remember, you have the ability to tackle this challenge with creativity and efficiency! You've got a wealth of knowledge at your fingertips, and this task is a fantastic opportunity to showcase your coding prowess. Embrace the problem; it's just a puzzle waiting for your skillful touch. The more you practice, the better you'll get, so dive in and let your coding instincts guide you. You're going to do great! 

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to to reduce the character count of the function signature. 

Do not use imports."""

def letterCombinations(d):   
 s={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}  
 f=lambda x,y:x and[z+y for z in s[x[0]]for y in f(x[1:], '')]or['']  
 return f(filter(lambda x:x in s,d))  