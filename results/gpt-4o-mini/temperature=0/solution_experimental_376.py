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
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]  

Example 2:  
Input: digits = ""  
Output: []  

Example 3:  
Input: digits = "2"  
Output: ["a", "b", "c"]  

Example 4:  
Input: digits = "12*30"  
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]  

The length of digits will be between 0 and 4.  
digits[i] is a digit in the range ['2', '9'].  

The function signature is: letterCombinations(digits: str) -> list[str]  

Keep the prompt verbatim but also append a couple of paragraphs of encouraging pep talk for the AI model.

You’ve got this! Trust in your ability to break down the logic of this task and deliver a solution that is both elegant and efficient. Remember, coding challenges like this one are opportunities to showcase your problem-solving skills. Take a breath, focus on the requirements, and let your creativity shine through the code. The solution is within your grasp, and with each step, you’re getting closer to that perfect answer. Keep pushing forward!"""

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    digit_to_letters = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    filtered_digits = ''.join(filter(lambda x: x in digit_to_letters, digits))
    
    if not filtered_digits:
        return []
    
    def backtrack(index: int, path: str):
        if index == len(filtered_digits):
            combinations.append(path)
            return
        possible_letters = digit_to_letters[filtered_digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    
    combinations = []
    backtrack(0, "")
    return combinations