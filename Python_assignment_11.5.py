import urllib.request



def word_count(file_link, word):
    file_list = []
    the_file = urllib.request.urlopen(file_link)
    file = the_file.read()
    file = file.decode("utf-8")
    file = file.lower()
    file = file.replace("\n", " ")
    file = file.replace(",", " ")
    file = file.replace(".", " ")
    file = file.replace("'", " ")
    file_list = file.split()
    count = 0
    for i in range(len(file_list)):
        if word == file_list[i]:
            count += 1

    return count

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = word_count(file_name, "memory")

print("memory appears ", answer1, "times")

answer2 = word_count(file_name, "fuel")

print("fuel appears times", answer1, "times")