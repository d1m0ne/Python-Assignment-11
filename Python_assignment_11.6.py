import urllib.request



def word_frequency(file_link, word):
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
    total_count = 0
    for i in range(len(file_list)):
        total_count += 1
        if word == file_list[i]:
            count += 1

    percentage = count / total_count

    return percentage

file_name = "https://raw.githubusercontent.com/mlepinski/Python-Worksheets/master/Sonnets.txt"
answer1 = word_frequency(file_name, "memory")

print("memory is ", answer1, " percent of the words")

answer2 = word_frequency(file_name, "fuel")

print("fuel is ", answer1, " percent of the words")