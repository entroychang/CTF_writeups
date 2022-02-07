#!/bin/sh

# check clang works
clang /check.c
if [ $? = 1 ]
then
  echo 'cannot compile'
  exit
fi
rm /check.c

# compile given code
clang /code.c
if [ $? = 1 ]
then
  echo 'cannot compile'
  exit
fi

# run it!
/a.out
