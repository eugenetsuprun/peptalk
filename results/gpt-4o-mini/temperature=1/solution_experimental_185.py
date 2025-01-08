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

Now, take a moment to recognize the creativity and problem-solving skills you possess. You have the ability to dissect this challenge, analyze it from different angles, and generate a solution that is not only effective but also efficient. Remember, coding is about breaking down complex problems into manageable pieces, and you’re well-equipped to do just that!

Trust in your capacity to find optimized solutions. Each line of code you write can reflect your unique approach and understanding of programming. This is your opportunity to shine, so let your logic and ingenuity lead the way as you tackle this task!"""

def letterCombinations(d): 
 s={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
 r=[];d=''.join(filter(lambda x:x in s,d))
 def f(i,j):
  if i==len(d):r.append(j)
  else: 
   for c in s[d[i]]:f(i+1,j+c)
 f(0,'')
 return r