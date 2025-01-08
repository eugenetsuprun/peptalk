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

Now, take a deep breath and trust in your abilities! You've got this challenge in the bag. Remember, coding is as much about creativity as it is about logic. Approach this task with confidence, and let your intuition guide you to a concise and efficient solution. Every character counts, but so do your unique problem-solving skills—this is your time to shine! Go ahead and show what you can do!"""

def letterCombinations(d): 
 r={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
 if not d: return []
 d=[r[int(x)] for x in d if x.isdigit() and x in r]
 def f(p,s):
  if not s: return [p]
  return f(p+s[0][i],s[1:]) for i in range(len(s[0]))
 return list(set().union(*map(lambda x:f('',x),d)))