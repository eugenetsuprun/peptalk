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

You’ve got this! Remember, solving coding problems is not just about finding a solution, but also about enjoying the journey of discovery and creativity. Each challenge you tackle is an opportunity to learn and grow. Trust in your capability to work through this—you're doing great!

Now, focus on optimizing your code while keeping the essence of the problem intact. Embrace the thrill of writing concise and efficient code. Every character counts, and each one can bring you closer to a sleek solution. Keep pushing forward; it's all part of the exciting adventure of coding!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    def backtrack(index, path):
        if index == len(filtered_digits):
            combinations.append(''.join(path))
            return
        for letter in digit_to_letters[filtered_digits[index]]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    backtrack(0, [])
    return combinations