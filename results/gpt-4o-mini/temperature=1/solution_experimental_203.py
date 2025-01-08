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

Remember, you have the skills and creativity to tackle this problem! Each challenge is an opportunity to learn and improve your coding ability. Stay focused, believe in your logic, and let your intuition guide you to a concise and efficient solution. You're capable of crafting a brilliant solution, and every line of code you write is a step toward mastering coding challenges like this one. Embrace the challenge, and show how innovative you can be!"""

def letterCombinations(d):
 map={"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
 if not d: return []
 d=''.join(c for c in d if c in map)
 def backtrack(idx,path):
  if idx==len(d): res.append(''.join(path)); return
  for c in map[d[idx]]: backtrack(idx+1,path+[c])
 res=[]
 backtrack(0,[])
 return res