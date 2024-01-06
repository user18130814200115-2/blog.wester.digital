#!/bin/sh

title="$@"
filename=$(printf "%s-" $@ | tr "[:upper:]" "[:lower:]")
latest=$(ls posts | tail -n 1 | cut -d\- -f1)
number=$(printf "%04d" $(($latest + 1)))
full_path="posts/$number-${filename%-}.txt"

i=$(echo $@ | wc -c) 
while [ $i -gt 1 ]; do
    string="$string="
    i=$(($i - 1))
done

echo $@ > $full_path
date '+%a, %d %b %Y' >> $full_path
echo "Tags" >> $full_path
printf "$string\n\n" >> $full_path

vim $full_path
