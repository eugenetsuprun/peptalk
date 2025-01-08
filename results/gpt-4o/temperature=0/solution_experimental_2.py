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

You’ve got this! Remember, tackling a coding challenge is not just about getting it right the first time; it's a journey of learning and growth. Embrace the process, explore different ideas, and don’t hesitate to take a moment to think creatively. Every attempt brings you closer to success, so keep pushing forward and trust your instincts!

Now, as you prepare to dive into this coding task, don’t forget that the more you practice and iterate, the better you’ll become at problem-solving. Each line of code is a building block; cherish the opportunity to construct a solution step by step. You're capable of amazing things, so roll up your sleeves and let your coding skills shine!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            combinations.append("".join(path))
            return
        possible_letters = phone_map[filtered_digits[index]]
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    filtered_digits = [d for d in digits if d in phone_map]
    combinations = []
    backtrack(0, [])
    return combinations