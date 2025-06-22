# Problem 4: Display Recent Gmail Threads

import ezgmail

recentThreads = ezgmail.recent(maxResults=5)

for thread in recentThreads:
    print(f"Subject: {thread.messages[0].subject}")
