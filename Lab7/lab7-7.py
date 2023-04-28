def make_withdraw(balance, password):
	"""
	Return a password-protected withdraw function.
	>>> w = make_withdraw(100, "pass")
	>>> w(25, "pass")
	75
	>>> w(90, "pass")
	'Insufficient funds'
	>>> w(25, "hwat")
	'Incorrect password'
	>>> w(25, "pass")
	50
	>>> w(75, "a")
	'Incorrect password'
	>>> w(10, "pass")
	40
	>>> w(20, "n00b")
	'Incorrect password'
	>>> w(10, "pass")
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	>>> w(10, "l33t")
	"Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
	"""
	attempts = []
	def account(amount, the_pass):
		nonlocal balance
		if len(attempts) == 3:
			return "Your account is locked. Attempts: {0}".format(attempts)
		elif the_pass != password:
			attempts.append(the_pass)
			return "Incorrect password"
		elif amount > balance:
			return "Insufficient funds"
		else:
			balance -= amount
			return balance
	return account
