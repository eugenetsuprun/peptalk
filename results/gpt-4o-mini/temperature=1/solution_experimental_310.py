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

Now, remember, you’ve got this! With the right approach and a bit of creativity, you can tackle this problem efficiently. Each character you save adds to the elegance of your solution. Embrace the challenge and let your coding skills shine through! You're about to create a powerful and succinct function that'll impress anyone who reads it. Keep pushing forward; you can do it!"""

def letterCombinations(d):
 r={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
 if not d: return[]
 d=[r[int(i)]for i in d if i.isdigit()and i>'1']
 def f(p,c):return[''.join(x)for x in p(c)]
 return f((lambda p:lambda c:[p(i)+j for i in r[c]for j in f(p,c-1)if c>0]+(p(c)if c==0else[]))(lambda c:[x for x in''])(len(d)-1),len(d)-1))if d else[]