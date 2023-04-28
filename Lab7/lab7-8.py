def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """

    attempts_pw = []
    attempts_count = 0
    
    def withdraw(amount, pw):
        
        nonlocal balance, attempts_pw, attempts_count, password
        
        if attempts_count >= 3: # account is locked
            
            return 'Your account is locked. Attempts: ' +  str(attempts_pw)
        
        else: # account is not locked
            
            if pw == password: # correct password
            
                if amount > balance: # insufficient funds
                    return 'Insufficient funds'
                    
                else: # sufficient funds
                    
                    balance = balance - amount # re-bind balance 
                    return balance
                
            else: # incorrect password
                
                # add incorrect password to attempts_pw vector and increase
                # attempts_count by 1
                attempts_count = attempts_count + 1
                attempts_pw = attempts_pw + [pw]
                
                return 'Incorrect password'
                
    return withdraw
        

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'
    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10
    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    
    incorrect = withdraw(0, old_password)
    if type(incorrect) == str: 
        return incorrect           
    else: 
        def joint(amount, pw):             
            if pw == new_password: 
                return withdraw(amount, old_password)
            else: 
                return withdraw(amount, pw) 
        return joint