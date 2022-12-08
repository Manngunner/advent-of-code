import re
from dataclasses import dataclass, field

@dataclass
class Directory:
    files: dict = field(default_factory=lambda : {})
    subdirectories: list = field(default_factory=lambda : [])
    parentdirectory: str() = ""
    listedbefore: bool = False

directories = {"/" : Directory()}

with open("Day 7/input.txt", "r", encoding="utf8") as inputfile:
    listing = False
    pwd = ["/"]
    allfiles = int()
    for line in inputfile.readlines():
        pwdstr = ''.join(pwd)
        while listing:
            if re.match("^\$", line.rstrip()):
                listing = False
                break
            directory = re.match("dir\s(\w+)", line.rstrip())
            if directory:
                if pwdstr+directory.group(1)+"/" not in directories:
                    directories.update({pwdstr+directory.group(1) + "/" : Directory(parentdirectory=pwdstr)})
                    continue
                directories.get(pwdstr).subdirectories.append(directory.group(1)+"/")
            file = re.match("(\d+)\s(.*)", line.rstrip())
            if file:
                directories.get(pwdstr).files.update({file.group(2) : file.group(1)})
                allfiles += int(file.group(1))
            break
        cd = re.match("^\$\scd\s(\w+|..)", line.rstrip())
        if cd:
            if cd.group(1) == "..":
                pwd.pop()
                continue
            pwd.append(cd.group(1) + "/")
        if re.match("^\$\sls", line.rstrip()):
            listing = True

results = {'/':0}
totalsize = int()
for string, directory in directories.items():
    if len(string[:-1]) == 0:
        dirpath = string
        for file in directory.files.values():
            results[dirpath] += int(file)
        continue
    dirpath = string[:-1]
    results.update({dirpath : int()})
    for file in directory.files.values():
        results[dirpath] += int(file)
    crawl = dirpath.rstrip().split("/")
    while crawl:
        crawl.pop()
        newdir = '/'.join(crawl)
        if newdir:
            results[newdir] += results[dirpath]
            continue
        crawl.pop()
        results['/'] += results[dirpath]

for dir, size in results.items():
    if size <= 100_000:
        totalsize += size

print(totalsize)