#!/usr/bin/env python3

with open("dracula.txt","r") as foo:
    for line in foo:
        if "vampire" in line.lower():
            print(line)
count= 0
for line in foo:
    if "vampire" in line.lower():
        count += 1
print(count)

