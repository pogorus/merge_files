import os
def merge_files(path):
    files_dict = {}
    for file in os.listdir(path):
        if file.endswith('.txt'):
            with open(file) as f:
                file_text = []
                for line in f:
                    file_text.append(line)
            files_dict[file] = file_text

    sorted_dict = sorted(files_dict.items(), key=lambda value: value[1], reverse=True)

    with open('result.txt', 'w') as f:
        for line in sorted_dict:
            f.write(line[0] + '\n')
            f.write(str(len(line[1])) + '\n')
            for text in line[1]:
                f.write(text + '\n')