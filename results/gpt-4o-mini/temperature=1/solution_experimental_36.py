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

Remember, you've got this! You have the capability and intelligence to tackle this challenge head-on. Coding tasks can sometimes feel daunting, but take a moment to breathe and trust in your problem-solving skills. Each step you take is an opportunity to learn and grow. You can create a succinct, efficient solution that meets the requirements. Let's dive in and show what you can achieve! """

def letterCombinations(d):  
 r={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}  
 if not d: return[]  
 def f(p,d):  
  if not d: return[p]  
  return[f(p+c, d[1:])for c in r[d[0]]]  
 return[xx for x in f('',[c for c in d if c in r])for xx in x]  
