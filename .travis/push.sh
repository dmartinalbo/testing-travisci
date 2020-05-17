#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  
  git remote rm origin
  git remote add origin https://dmartinalbo:${GH_TOKEN}@github.com/dmartinalbo/testing-travisci.git > /dev/null 2>&1
}

bump_version() {
  git checkout master
  bump2version minor --allow-dirty --verbose --tag-name 'v{new_version}' --message "[skip ci] Bump to v{new_version}"
}

merge() {
  git checkout -B stable
  git merge --no-ff -m "[skip ci] merging 'master' into 'stable'" stable 
}

push_changes() {
  git push --quiet origin master stable --tags 
}

setup_git
bump_version
merge
push_changes

