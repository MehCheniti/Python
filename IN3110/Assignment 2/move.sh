#!/bin/bash

function move {
  # Configuring the environment.
  dir="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd )"/
  # Creating source command line.
  src=$1
  # Creating destination command line.
  dst=$2
  arr=()

  # Checking if source directory exists.
  if [ -d "$dir$src" ]; then
    arr+=("$dir$src")
  else
    if [ ! -d "$dir$src" ]; then
      echo "Enter a directory that exists."
      read newSrc;
      src=$newSrc;
      arr+=("$dir$src")
    fi
  fi

  # Checking if destination directory exists.
  if [ -d "$dir$dst" ]; then
    arr+=("$dir$dst")
  else
    if [ ! -d "$dir$dst" ]; then
      # Creates directory that has the name of the current date and time.
      DATE=$(date '+%Y-%m-%d-%H:%M:%S')
      mkdir "$DATE"
      dst="$DATE"
      arr+=("$dir$dst")
    fi
  fi

  # Checking that there are 2 command line arguments.
  if [ "${#arr[@]}" == "2" ]; then
    # Giving the user the option to move all files.
    echo "Input 'all' if you want to move all files in a directory, or 'no' if you don't want to."
    read answer
    if [ "$answer" == "all" ]; then
      mv $src/* $dst -i
    else
      mv ${arr[0]} ${arr[1]}
    fi
  fi
}
