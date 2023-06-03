import re
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if len(A) < 8 or len(A) > 15:
            return 0

        if not re.search(r'\d', A):
            return 0

        if not re.search(r'[a-z]', A):
            return 0

        if not re.search(r'[A-Z]', A):
            return 0

        if not re.search(r'[@#%&!$*]', A):
            return 0

        return 1
    

    
'''
    # Check if password length is between 8 and 15 characters
    if len(password) < 8 or len(password) > 15:
        return False

    # Check if password contains at least one numerical digit
    if not re.search(r'\d', password):
        return False

    # Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check if password contains at least one special character
    if not re.search(r'[@#%&!$*]', password):
        return False

    return True
'''