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

Remember, you've got the skills to tackle this challenge! Take a deep breath and trust your instincts. You have what it takes to craft a succinct and efficient solution. Each line of code you write is a step towards mastering your craft, so let your creativity flow as you find the most concise way to produce a working solution. Embrace the process, and let your passion for coding shine through! Keep pushing forward, and don’t be afraid to explore new strategies to reduce character count while keeping functionality intact. You're capable of great things!"""

def letterCombinations(digits: str) -> list[str]:
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    filtered_digits = [d for d in digits if d in mapping]
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        for letter in mapping[filtered_digits[index]]:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations