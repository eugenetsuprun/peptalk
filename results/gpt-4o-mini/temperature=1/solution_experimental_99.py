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

You've got this! Remember, every challenge is an opportunity to grow and learn something new. Embrace the task ahead with enthusiasm, and don’t hesitate to think outside the box as you craft your solution. Keep in mind that coding is not just about getting the right answer, but also about finding efficient and elegant ways to express your ideas. Trust in your ability to bring creativity and precision to your coding process, and enjoy the journey!"""

def letterCombinations(d):return[]if not delse__import__('itertools').product(*'abc def ghi jkl mno pqrs tuv wxyz'.split()[int(c)-2]for c in d if'2'<=c<='9') else[''.join(p)for p in _]