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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature as described above but other than that, take any shortcuts you need to to reduce the character count of the function. 

Do not use imports.

Remember, you've got this! You've tackled challenges before, and every problem you face is an opportunity to shine. Trust in your abilities, and don’t hesitate to draw on your knowledge. Your creativity and logic are your greatest assets. You’re not just solving a problem; you’re creating a solution that others can learn from and appreciate. Embrace the challenge and keep pushing forward!"""

def letterCombinations(digits: str) -> list[str]:
    m={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    res=['']
    for d in digits:
        if d in m:
            res=[p+c for p in res for c in m[d]]
    return res