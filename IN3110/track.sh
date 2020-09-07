#!/bin/bash

function start {
  LOGFILE=".local/share/logfile.txt"
  echo "Input task number."
  read label
  label=$1

  if [ -z $label ]; then
    echo -e "START $(date) \nLABEL This is task $label" >> $LOGFILE
  else
    echo "ERROR, there is already a task running."
  fi
}

function stop {
  echo -e "END $(date) \n" >> $LOGFILE
}

function status {
  if [ -z $label ]; then
    echo "Active task: $label"
  fi
}
