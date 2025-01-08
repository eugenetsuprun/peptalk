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

Remember, you’ve got this! This problem may seem challenging at first, but break it down step by step, and you’ll find that with each small victory, you'll be getting closer to a complete solution. Embrace the process and give it your best effort—every character counts, and you have all the skills needed to create something efficient and elegant.

So dive in and have fun with the problem! Trust your intuition and let your creativity guide you to a solution that not only works but also showcases your coding prowess. You’ve got what it takes to tackle this—now go for it!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_mapping = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    # Filter out non-digit characters and zeros/ones
    digits = ''.join(filter(lambda x: x in phone_mapping, digits))

    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        for letter in phone_mapping[digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    backtrack(0, [])
    return combinations