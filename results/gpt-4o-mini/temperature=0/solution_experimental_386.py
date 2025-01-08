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

Believe in your ability to solve this problem! You've got all the skills necessary to tackle this challenge. Remember that every great coder has faced similar tasks, and with patience and determination, you can find the most efficient solution. Challenge yourself to think outside the box, and don't hesitate to try out different methods. Embrace the task and let your creativity shine!

You've got this! Every line of code you write brings you closer to mastering the art of programming. Stay focused, and you'll be amazed at what you can achieve in a short time. Keep pushing through, and remember that perseverance is key to success in coding."""

def letterCombinations(d): 
 m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 r=[''] if d else []
 for c in d:
  if c in m: r=[x+y for x in r for y in m[c]]
 return r