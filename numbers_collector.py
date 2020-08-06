'''

function printData() {
    let t = document.getElementsByClassName('reactable-data')

    for (row of t[0].children) {
        console.log(row.cells[1].innerHTML)
    }
}
'''

s = open("data.txt", "r").read()

nums = ""

for line in s.split("\n"):
    num = line.split(" ")[1]
    if len(num) < 4:
        num = "0" * (4 - len(num)) + num

    nums += num + " "

with open('topic_questions_id.txt', 'a+') as fp:
    fp.write("Recursion" + "=" + nums + "\n")
