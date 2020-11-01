import urllib.request



def count_lines(file_link):

    file = urllib.request.urlopen(file_link)
    count = 0
    for line in file:
        line = line.decode("utf-8")
        count += 1

    return count

file_name1 = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = count_lines(file_name1)

file_name2 = file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/coolWords.txt"
answer2 = count_lines(file_name2)

print("First file number of lines:" , answer1)
print("Second file number of lines:" , answer2)

