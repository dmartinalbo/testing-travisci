#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout master
  echo "testing" >> foo.txt
  git add foo.txt
  git commit -m "Travis did this. Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote rm origin
  git remote add origin https://dmartinalbo@${GH_TOKEN}@github.com/dmartinalbo/testing-travisci.git > /dev/null 2>&1
  git push --quiet origin master 
}

setup_git
commit_website_files
upload_files

