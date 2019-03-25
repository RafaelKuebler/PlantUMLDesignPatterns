import os
import json
import hashlib
import subprocess

# https://stackoverflow.com/questions/3431825/generating-an-md5-checksum-of-a-file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    
    
data = {}

# load config if it exists
data_exists = os.path.isfile('data.json')
if data_exists:
    with open('data.json', 'r') as fp:
        data = json.load(fp)

for file in os.listdir():
    if file.endswith(".txt"):
        # run plantuml if diagram is new or has changed
        hash = md5(file)
        has_changed = hash != data[file]
        not_existing = not os.path.isfile('./output/{}'.format(file.replace('txt', 'png')))
        
        if has_changed or not_existing:
            print("Processing {}".format(file))
            subprocess.run(['java', '-jar', 'plantuml.jar', '-duration', '-o', './output', file])
        data[file] = hash

# save hashes
with open('data.json', 'w') as fp:
    json.dump(data, fp, sort_keys=True, indent=4)
