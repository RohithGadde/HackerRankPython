def split_and_join(line):
    y = line.split(" ")
    x = "-".join(y)
    return x


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
