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

Remember, coding challenges can seem daunting, but you have the skills and creativity to tackle this problem head-on. Take a moment to breathe and visualize your approach before jumping into the writing phase. Each challenge is just a stepping stone toward improving your problem-solving abilities, so let's unleash your potential and create a solution that shines!

Trust in your experience and intuition. You are more than capable of optimizing this function while maintaining clarity. Embrace the challenge, and have fun crafting a solution that not only meets the requirements but also showcases your unique coding style!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = [d for d in digits if d in digit_to_char]
    if not filtered_digits:
        return []

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            combinations.append(combination)
        else:
            for letter in digit_to_char[next_digits[0]]:
                backtrack(combination + letter, next_digits[1:])

    combinations = []
    backtrack("", filtered_digits)
    return combinations