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

Now, you’re stepping into a challenge that may seem daunting, but remember that every small step you take leads you closer to success. You have the skills and insight to tackle this coding task, and as you type out the solution, visualize the elegance of your code coming together. Stay confident and creative, trusting in your ability to navigate through the logic and find efficient solutions.

Embrace this problem as an opportunity to showcase your problem-solving prowess! Each line of code is a chance to express your understanding of algorithms and data structures. With focus and determination, you're not just solving a challenge; you're sharpening your skills and preparing for the exciting hurdles ahead. Go for it!"""

def letterCombinations(d): 
    m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'} 
    res = [''] if d else [] 
    for c in d: 
        if c in m: 
            res = [p + q for p in res for q in m[c]] 
    return res 