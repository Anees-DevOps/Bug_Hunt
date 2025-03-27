# Steps to follow:
bug-app % git init

git status
#On branch master

git add . # Add all the code changes to staging area for committing

git checkout -b main # Switch to main branch

git remote add origin git@github.com:Anees-DevOps/Bug_Hunt.git # Connect to github repo - Remote.

git commit -m "Fixed bug hunt" # commit your changes to remote repo.

git push -u origin main # Push your final changes after fixing the bug to update ur remote repo.
