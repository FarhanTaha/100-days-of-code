# Problem 3: Print Subjects of Unread Emails

import ezgmail

unreadThreads = ezgmail.unread()

for thread in unreadThreads:
    for message in thread.messages:
        print(f"Subject: {message.subject}")
