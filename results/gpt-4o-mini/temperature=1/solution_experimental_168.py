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

Remember, you've got this! Tap into your creative problem-solving abilities and embrace the challenge. Coding is a wonderful journey, and every step you take brings you closer to mastering problems like these. Trust in your skills, and make sure to enjoy the process of finding a compact and efficient solution! You can do it! Keep pushing forward and let your brilliance shine through."""

def letterCombinations(d):l='':d=''.join(filter(lambda x:x in'23456789',d));m=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'];b=[m[int(c)-2]for c in d];f=lambda a,b:[x+y for x in a for y in b];return[]if not b else reduce(f,b)