import os
import random
from datetime import datetime, timedelta

start_year = 2018
end_year = 2022

# List of months you want to include (1-12)
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# List of days you want to include (1-31)
days = list(range(1, 28))

max_commits_per_day = 2  # Adjust this to specify the maximum number of commits per day

for i in range(2):
    # Generate a random date within the specified range
    year = random.randint(start_year, end_year)
    month = random.choice(months)
    day = random.choice(days)

    # Create a datetime object for the commit date
    commit_date = datetime(year, month, day)

    # Calculate the difference in days
    days_ago = datetime.now() - commit_date

    # Convert days_ago to a string like 'X days ago'
    d = str(days_ago.days) + ' days ago'

    # Specify the number of commits for this day
    num_commits = random.randint(1, max_commits_per_day)

    # Print a message for each commit
    for j in range(num_commits):
        print(f"Committing on {commit_date}")

        # Append the commit date to the file for the specified number of commits
        with open('test.txt', 'a') as file:
            file.write(d + '\n')

        # Add, commit, and push the changes for each commit
        os.system('git add test.txt')
        os.system(f'git commit --date="{commit_date}" -m 1')

# Push the changes to the repository
os.system('git push -u origin main -f')
