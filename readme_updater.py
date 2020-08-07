import os

header = """# Leetcode Solutions

This repository contains my solutions to leetcode problems. You can find my leetcode profile [here](https://leetcode.com/AtharvRedij/).

| Topic | Questions |
| ----- | --------- |
"""

with open('README.md', 'w') as readme1:
    readme1.write(header)

fp = open('topic_questions_id.txt', 'r')

for f in fp:
    parts = f.split("=")
    topic, ids = parts[0], parts[1].split(" ")[:-1]

    res = ""

    for f in os.listdir("."):
        for i in ids:
            if f.startswith(i):
                res += "[{}](<./{}>), ".format(f[5:-3], f)

    with open('README.md', 'a+') as fp1:
        fp1.write("| " + topic + " | " + res + " | " + "\n")
