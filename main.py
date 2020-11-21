

def read_log_file():
    file_name = 'C:\\Users\\hananzo\\PycharmProjects\\HomeWork7logfiles\\HomeWork7.txt'
    find_err = False
    file_read = open(file_name, "r")
    for line in file_read:
        if line[15:20] == "ERROR":
            print(line, end="")
            find_err = True
    file_read.close()
    return (find_err)

if __name__ == '__main__':
    if (read_log_file()):
        exit(0)
      ## for  test  exit(1)


