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

You’ve got this! Tackling coding challenges can be tough, but remember that each problem is an opportunity to learn and grow. Trust in your ability to break down the task step by step and think creatively about how to optimize your solution. 

Stay focused and keep a positive mindset! Every keystroke brings you closer to a solution. Embrace the challenge, and don’t hesitate to explore different approaches. You can create a compact and efficient solution that impresses!"""

def letterCombinations(d):return[''.join(p)for i in filter(str.isdigit,d)for p in[(c1+c2)for c1 in'abc'if(i:='23456789'[int(i)-2])for c2 in'abc'[(ord(i)-ord('2'))*3:ord(i)>='7'and(ord(i)-ord('2'))*3+4or(ord(i)-ord('2'))*3+3)]]if i]