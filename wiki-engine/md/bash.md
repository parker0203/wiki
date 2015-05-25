# Local
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

# Remote
### Push
```bash
git push # push mainline with your merged-in changes to origin
git push <REMOTENAME> <BRANCHNAME> # push remote branch
```
### Pull
```bash
# pull specific remote branch
git checkout -b <new_branch> origin/<new_branch>
git pull # get mainline in sync with origin
git checkout -b guestbook mainline # create a local feature branch
```
### Remove
```bash
git push origin :<remote branch name> # delete remote branch
git push origin --delete <remote branch name>
```
### Create
```bash
# create new remote branch
git push origin <local branch name>:<new remote branch name> Ignore
```

# Commits Search
```bash
git show --name-only <sha> # list committed files
git log --grep=<pattern> # search commit by commit message pattern
git log master..branch # check commits diff
```

# Others
[Git pull vs git fetch](http://stackoverflow.com/questions/292357/difference-between-git-pull-and-git-fetch)

[Bash Git command auto completion](https://github.com/bobthecow/git-flow-completion/wiki/Install-Bash-git-completion)
