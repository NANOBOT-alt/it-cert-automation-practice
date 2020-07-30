#!/usr/bin/env python3

import re
ans = True
def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    # Usernames can only use letters and  numbers
    if  re.match('^[a-z0-9]*$', username):
        ans = True
    # Username can't begin with . or _
    elif re.match('^[._]*$', username):
        ans = False
    else : ans = True
    return ans

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False


