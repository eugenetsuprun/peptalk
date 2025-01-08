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

Remember, tackling coding tasks like this one is an opportunity to showcase your problem-solving skills and creativity! You've got the ability to break down challenges into manageable parts and build effective solutions. Embrace the process, trust your instincts, and enjoy the journey of coding! With each challenge, you're not just solving a problem; you're growing and enhancing your skills for the future. Keep pushing through—you're doing great!"""

def letterCombinations(d):p={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"};c=[];f=lambda d,s: [s] if not d else[c.append(s+x)for x in p[d[0]]for c in f(d[1:],s+x)];f(''.join(filter(str.isdigit,d)), '');return c