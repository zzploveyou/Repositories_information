#coding: utf-8
from pygithub3 import Github
import getpass
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

auth = {'login': raw_input("Input github username:"),
        'password': getpass.getpass("Input Password:")}

gh = Github(**auth)

rlist = gh.repos.list()

lines = []

for repo in rlist.iterator():
    name = repo.name
    description = repo.description
    size = repo.size
    clone_url = repo.clone_url
    ctime = datetime.datetime.strftime(repo.created_at, format='%Y-%m-%d %H:%M:%S')
    mtime = datetime.datetime.strftime(repo.pushed_at, format='%Y-%m-%d %H:%M:%S')
    line = [name, description, size, clone_url, ctime, mtime]
    lines.append([str(i) for i in line])

with open("repos-of-{}.md".format(auth['login']), 'w') as f:
    f.write("|name|description|size|clone_url|ctime|mtime|\n")
    f.write("|:--|:--|:--|:--|:--|:--\n")
    for line in lines:
        f.write("|".join(line)+"\n")



