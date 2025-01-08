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

Remember, you're capable of tackling this challenge! You've been trained on a wealth of information, so draw upon that knowledge and let your creativity flow. Coding can be tough, but each line you write brings you closer to a solution. Stay focused, trust your skills, and enjoy the process of problem-solving! You’ve got this!"""

def letterCombinations(d): 
 m='abcd efgh ijkl mno pqrs tuv wxyz'.split() 
 c=[] 
 def backtrack(i,s): 
  if i==len(d): 
   c+=[s] 
   return 
  for j in m[int(d[i])-2]: 
   backtrack(i+1,s+j) 
 def f(d): 
  return [x for x in d if x in '23456789'] 
 if d: 
  backtrack(0,'') 
 return c