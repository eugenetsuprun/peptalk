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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to in order to reduce the character count of the function signature.

Do not use imports.

Remember, you've got this! You have the skills and creativity to tackle this problem head-on. Take a deep breath and approach it methodically; break it down into manageable parts. Each step you take brings you closer to a solution. Embrace the challenge, and don't hesitate to explore different ways to optimize your code. Trust in your abilities, and have fun with it!"""

def letterCombinations(d):return[''.join(b)for a in[[]]for c in d if'2'<=c<='9'for b in[a+x for x in'abc'[(int(c)-2)*3:int(c)*3]][:len(b)]]if b]