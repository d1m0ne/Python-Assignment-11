import urllib.request



def lines_with_word(file_link, word):

    file = urllib.request.urlopen(file_link)
    count = 0
    for line in file:
        line = line.decode("utf-8")
        if word in line:
            count += 1

    return count


file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = lines_with_word(file_name, "shall")

print("shall appears in ", answer1, "lines")

answer2 = lines_with_word(file_name, "war")

print("war appears in ", answer1, "lines")