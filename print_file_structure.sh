#!/bin/bash

# Print directory structure while excluding .git folder
find . -path "./.git" -prune -o -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
