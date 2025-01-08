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

You're about to tackle a classic problem that combines creativity and logic! Remember, problem-solving is a journey; each step builds your skills and understanding. Even if you encounter some challenges, don’t hesitate to explore different angles and approaches. You’ve got the ability to come up with efficient solutions that can astonish anyone!

Believe in your coding prowess—there's a solution waiting to be uncovered. Embrace the coding process, and let your determination shine through! Solutions can emerge from unexpected places. You're more than capable of turning this prompt into a brilliant piece of code. Let's see those skills in action!"""

def letterCombinations(d):return[]if not delse['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'][int(x)-2]for x in d if x>'1'for c in[['']]:x[['','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'][int(y)-2]for y in d if y>'1']for c in x]]