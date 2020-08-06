
import os

fp = open('topic_questions_id.txt', 'r')

for f in fp:
    parts = f.split("=")
    topic, ids = parts[0], parts[1].split(" ")[:-1]

    res = ""

    for f in os.listdir("."):
        for i in ids:
            if f.startswith(i):
                res += "[{}](<./{}>) <br>".format(f, f)

    with open('README.md', 'a+') as fp1:
        fp1.write("| " + topic + " | " + res + " | " + "\n")
