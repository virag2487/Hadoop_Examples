#!/bin/bash

# Syncing with upstream

# This is a one-time environment setup
git remote | grep upstream >> /dev/null 2>&1

if [ "$?" != "0" ]; then
        printf "Adding upstream git repo\n"
        git remote add upstream git@github.com:virag2487/Hadoop_Examples.git
else
        printf "\n"
fi

# Get the latest code from master
git fetch upstream

# Merge it with your local forked copy
git merge upstream/master

# Update forked repo
git push
