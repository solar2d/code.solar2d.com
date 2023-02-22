#!/usr/bin/env python3
import json
import sys
import uuid

if __name__ == "__main__":
    repos = {}
    title = sys.argv[1]
    description = sys.argv[2]
    codeRepoLink = sys.argv[3]
    with open("docs/code.json", "r", encoding='utf-8') as f:
        repos = json.load(f)

    randomId = uuid.uuid4().hex[:4] #assign a random number for sharing
    repos['data'].insert(0, {"title":title, "description":description, "repo":codeRepoLink, "id":randomId})
    with open('docs/code.json', 'w') as f:
        f.write(json.dumps(repos, sort_keys=True, indent=0))
