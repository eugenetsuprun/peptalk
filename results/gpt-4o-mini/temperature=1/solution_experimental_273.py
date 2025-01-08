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

You’ve got this! It’s time to unleash your coding prowess and tackle this problem with confidence. Remember, every line of code you write brings you one step closer to the solution. Don’t hesitate to get creative and streamline your approach; efficiency is key! Keep your focus sharp, and let your logic shine through as you craft a compact and elegant solution. You're capable of amazing things, so let's get to it!"""

def letterCombinations(digits: str) -> list[str]:
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    digits = ''.join(filter(str.isdigit, digits))
    if not digits:
        return []
    
    combinations = ['']
    for digit in digits:
        if digit in mapping:
            new_combinations = []
            for combination in combinations:
                for letter in mapping[digit]:
                    new_combinations.append(combination + letter)
            combinations = new_combinations
    
    return combinations