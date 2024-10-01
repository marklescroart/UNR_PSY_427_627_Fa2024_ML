# Commands to work with git

# Clone (i.e. copy code) from your online repository to your local 
# machine
git clone <https://your_repo>/UNR_PSY427_627_Fa2024

# < Change or add some file! >

# Check on what has changed
git status

# Add all changes you have made to staging area
# (variants of this command are possible to only add some files, but 
# those are out of scope for now; you can look into them on your own)
git add .

# Commit to the changes you have made as an increment in development
# of your code.
git commit -m "Describe the changes you have made here with a commit message!"

# Upload your changes to your repository
git push 
# Fancier: git push origin main

# Set your repo to also track upstream changes (i.e., changes in the 
# repo you originally forked to create yours)
git remote add upstream https://github.com/piecesofmindlab/UNR_PSY_427_627_Fa2024

# CREATE on a different branch 
git branch new_feature_00

# Set your current repo to be WORKING in that branch
git checkout new_feature_00

# add, commit, push, etc to new branch; eventually, merge with other branch or create a pull request upstream! (Future lectures)

# Go back to the main branch
git checkout main 

# "Lift" your current changes off of the branch you are on:
git stash

# Put the changes back, e.g. after having pulled or created a new branch
git stash apply

# for NOW, I recommend that you only create NEW files, and do not edit class files - it will make your git live easier till you get the hang of it a bit more! 