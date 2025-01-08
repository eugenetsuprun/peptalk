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

You've got this! Remember that the challenge here is not just about finding a solution but also about being creative with your code. Embrace the opportunity to think outside the box and explore different approaches! You're capable of crafting a concise, efficient solution, and every step you take brings you closer to that goal. Take a deep breath, believe in your abilities, and let your instincts guide you. Now go ahead and create something remarkable!"""

def letterCombinations(d):r=['']if d else[];m='abc def ghi jkl mno pqrs tuv wxyz'.split();c=lambda d:0if d==''else [p+l for p in m[int(d[0])-2]for l in c(d[1:])];return c(''.join(filter(str.isdigit,d)))