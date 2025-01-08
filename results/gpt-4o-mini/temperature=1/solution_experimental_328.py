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

---

You're about to tackle a coding challenge that offers a great opportunity to showcase your problem-solving skills! Remember, the task at hand may seem complex, but breaking it down into smaller parts will make it more manageable. Have confidence in your abilities—many have faced similar challenges and emerged victorious. Embrace the process of coding as a journey of exploration and creativity.

As you embark on crafting your solution, think about the various approaches you can take. You'll have the chance to be ingenious and efficient, so trust in your instincts. This is a chance not only to solve the problem but also to express your unique style as a coder. So go for it—your solution is within reach!"""

def letterCombinations(d):p={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'};r=[];d=''.join(filter(lambda x:x in p,d));def f(s,t):t=t or[''];c=p.get(s[0],[]);f(s[1:],[x+y for x in t for y in c])if s else r.extend(t);f(d,[]);return r