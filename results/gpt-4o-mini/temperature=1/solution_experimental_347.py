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

Remember, you’ve got this! Tackle the problem confidently, and don’t be afraid to think outside the box. Your skills are more than enough to navigate through this task—just take it one step at a time and trust in your ability to find efficient solutions. Every challenge is an opportunity to grow, so embrace it fully and let your coding prowess shine!"""

def letterCombinations(d):return[]if not(d:=[c for c in d if'2'<=c<='9'])else[''.join(x)for x in[(b,l)for b in d for l in'abc'[(int(b)-2)*3:int(b)*3]for o in'{}'for w in l]]for i in[0]]