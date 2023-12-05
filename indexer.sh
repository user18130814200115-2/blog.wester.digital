#!/bin/sh

cd Posts
ls -cr ./ | head -n 10 | xargs head -n 3 > ../index.txt
cd ..
