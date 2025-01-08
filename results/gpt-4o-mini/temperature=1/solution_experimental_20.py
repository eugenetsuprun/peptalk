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

As you embark on this coding challenge, remember that every line of code is a step toward clarity and solutions. Embrace the process of breaking down the problem and transforming it into a working piece of logic. You have the creativity and skills to think outside the box and find efficient solutions, even in the smallest spaces of code. 

Trust in your ability to solve this problem with finesse. Each character matters, but so does your intuition for the right approach. You've got this!"""

def letterCombinations(d):
 r=['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
 if not d: return []
 d=[r[int(x)-2] for x in d if x.isdigit()and x>'1']
 from itertools import product
 return [''.join(p)for p in product(*d)]