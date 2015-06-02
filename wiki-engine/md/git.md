```bash
git add -A # stages All, is equivalent to "git add .; git add -u"
git add . # stages new and modified, without deleted
git add -u # stages modified and deleted, without new
git checkout mainline # switch to mainline
# merge in your feature branch
git merge guestbook -m "Your merge message"
git merge --squash <branch-name>
git merge --abort
git rebase
git reset --hard <commit>
git diff mainline/<commit>
git diff --cached # See staged diff
git diff --name-only # show changed files
git branch
git branch -r # show remote branches
git branch -a # show remote & local branches
git branch -vv
git reset HEAD~1 # undo last commit
# if you want remove a commit from remote branch, run this, commit and push
git revert <commit>
# directly commit all modified files
git commit -am "<commit-message>"
# Single file difference between branches:
git diff branch1 branch2 -- filename
# Remove all Changes including new files
git reset --hard # removes staged and working directory changes
git clean -f -d # remove untracked files
# Merge a single commit from another branch
git cherry-pick COMMIT_HASH
```
