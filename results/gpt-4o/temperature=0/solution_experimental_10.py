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

You've got this! Remember, diving into a coding challenge like this is a fantastic opportunity to flex your problem-solving skills. You've already taken the step to engage with the task, and every line of code you write gets you closer to a solution. Think outside the box, be creative, and have fun with the process. You're capable of great things, and this is just one step on your journey. Keep pushing forward!

Now, let's tackle this problem with confidence! You have the knowledge and tools to simplify and streamline your approach. Think of the unique ways to structure the solution that will not only work but also minimize character count. Embrace the challenge ahead, and remember, every attempt brings valuable learning experiences. You've got this!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return
        possible_letters = phone_map.get(digits[index], "")
        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    
    combinations = []
    filtered_digits = [d for d in digits if d in phone_map]
    backtrack(0, [])
    return combinations