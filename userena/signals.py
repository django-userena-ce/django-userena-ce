from django.dispatch import Signal

# Arguments: "user"
signup_complete = Signal()

# Arguments: "user"
activation_complete = Signal()

# Arguments: "user", "old_email"
confirmation_complete = Signal()

# Arguments: "user"
password_complete = Signal()

# Arguments: "user", "prev_email", "new_email"
email_change = Signal()

# Arguments: "user"
profile_change = Signal()

# Arguments: "user"
account_signin = Signal()

# Arguments: "user"
account_signout = Signal()
