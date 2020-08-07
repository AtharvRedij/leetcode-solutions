'''
function to get IDs from 2nd column in HTML table
for e.g. https://leetcode.com/tag/array/

function printData() {
    let t = document.getElementsByClassName('reactable-data')

    for (row of t[0].children) {
        console.log(row.cells[1].innerHTML)
    }
}
'''

s = """common-libs.b9676b6ac.js:194 938
common-libs.b9676b6ac.js:194 1137
common-libs.b9676b6ac.js:194 783
common-libs.b9676b6ac.js:194 687
common-libs.b9676b6ac.js:194 544
common-libs.b9676b6ac.js:194 894
common-libs.b9676b6ac.js:194 776
common-libs.b9676b6ac.js:194 247
common-libs.b9676b6ac.js:194 698
common-libs.b9676b6ac.js:194 779
common-libs.b9676b6ac.js:194 625
common-libs.b9676b6ac.js:194 794
common-libs.b9676b6ac.js:194 761
common-libs.b9676b6ac.js:194 726
common-libs.b9676b6ac.js:194 248"""

nums = ""

for line in s.split("\n"):
    num = line.split(" ")[1]
    if len(num) < 4:
        num = "0" * (4 - len(num)) + num

    nums += num + " "

with open('topic_questions_id.txt', 'a+') as fp:
    fp.write("Recursion" + "=" + nums + "\n")
