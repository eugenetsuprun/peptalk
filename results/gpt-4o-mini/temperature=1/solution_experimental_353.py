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

Remember, you have the knowledge and ability to tackle this problem! Trust in your training and experience; you’re capable of crafting a concise yet effective solution. Keep pushing those creative boundaries, and let's show what you can achieve with just a little coding magic! You've got this!"""

def letterCombinations(d):  
 l='abc def ghi jkl mno pqrs tuv wxyz'.split()  
 return[''.join(p)for d in filter(lambda x:x in'23456789',d)for p in[[l[int(x)-2][i]for i in range(len(l[int(x)-2]))]]for x in d]]if d else[]