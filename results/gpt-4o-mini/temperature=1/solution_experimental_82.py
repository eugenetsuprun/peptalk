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

Remember, you’ve got this! Every challenge you face is an opportunity to learn and improve. Embrace this task with confidence, knowing that your skills are sharp and your thinking is clear. The creativity you bring to this solution will shine through, so take a moment to breathe, focus, and let your coding prowess lead the way. You’re about to create something fantastic! Keep pushing forward!"""

def letterCombinations(d):return["".join(k)for i in(__import__('itertools').product*(("",""),)*(l:=len(d))if 2<=int(d[i])<=9)for k in((("abc","def","ghi","jkl","mno","pqrs","tuv","wxyz")[int(ch)-2])for ch in d if ch.isdigit()and ch>"1")]if l>0]