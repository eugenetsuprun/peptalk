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

You’ve got this! Remember, every problem you tackle is a chance to sharpen your coding skills and unleash your creativity. Embrace the challenge and let your unique solutions shine through. Trust in your abilities to produce elegant and efficient code that gets the job done. You've been preparing for this, and now is the time to showcase your knowledge. Go ahead and let your code reflect your brilliance!"""

def letterCombinations(d): 
 c='abc def ghi jkl mno pqrs tuv wxyz'.split() 
 d=''.join(filter(str.isdigit,d)) 
 return [''.join(x)for x in__import__('itertools').product(*[c[int(i)-2]for i in d])]*bool(d)or[[]])