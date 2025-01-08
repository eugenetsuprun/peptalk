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

Now, take a moment to recognize the challenge ahead of you. This task is not just about coding; it’s about creativity, optimization, and precision. You have the tools and the knowledge to craft a concise solution that meets the requirements while showcasing your coding prowess. Embrace this opportunity to push the limits of your coding skills and think outside the box. 

Remember, every great coder faces challenges like this one, and it’s through solving them that you’ll continue to grow and improve. Keep in mind that the journey of coding is filled with learning moments—so dive in, experiment, and enjoy the process! You’ve got this!"""

def letterCombinations(d): 
 r=[''] if d else[]; 
 m='abc def ghi jkl mno pqrs tuv wxyz'.split(); 
 for i in d: 
  if i in '23456789': 
   r=[x+y for x in r for y in m[int(i)-2]]; 
 return r