#!/usr/bin/env python3
import json
import sys


if __name__ == "__main__":
    repos = {}
    title = sys.argv[1]
    description = sys.argv[2]
    codeRepoLink = sys.argv[3]
    with open("docs/code.json", "r", encoding='utf-8') as f:
        repos = json.load(f)

    repos['data'].insert(0, {"title":title, "description":description, "repo":codeRepoLink})
    with open('docs/code.json', 'w') as f:
        f.write(json.dumps(repos))
