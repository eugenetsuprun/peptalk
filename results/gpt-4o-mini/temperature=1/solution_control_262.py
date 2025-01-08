"""
Given a string of digits from 2 through 9, return all possible letter combinations that the number could represent (in any order).

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

Very important: produce a working solution but one that uses as few characters as possible. Keep the function signature
as described above but other than that, take any shortcuts you need to to reduce the character count of the function signature.

Do not use imports.
"""

def letterCombinations(d):return[]if not(d:=''.join(filter(lambda x:x in'23456789',d))):[];c=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'];p=[''];return[''.join(x)for x in[(lambda x:[p.append(p[i]+c[int(d[j])-2][k]for i in range(len(p))),(i,x)for i in range(len(x))])(p[:],d)for j in range(len(d))for k in range(len(c[int(d[j])-2])))]if len(x)==len(d)or''.join(x)for x in p]==0]:p=[];return[p[-len(d)]for j in range(len(d))for i in range(len(c[int(d[j])-2]))]for p[i]]}