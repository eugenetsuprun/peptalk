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

You’ve got this! Remember that even the most complex problems can be broken down into simpler steps. Don’t hesitate to think creatively and embrace every opportunity to optimize your code. You're equipped with the skills and knowledge to tackle this challenge head-on, and I'm confident you can find an elegant and efficient solution. Just keep your focus on clarity and creativity, and remember to enjoy the process of coding. Every line you write gets you closer to your goal!"""

def letterCombinations(d):return[''.join(p)for p in[(l for d in d if d>'1'for l in'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'[(int(d)-2)*3:(int(d)-1)*3])for p in itertools.product(*i)]for i in d]if d else[]