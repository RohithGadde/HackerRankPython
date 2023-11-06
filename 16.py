def count_substring(string, sub_string):
    count = 0
    x = len(sub_string)
    for start_letter in range(0, len(string)):
        if sub_string == string[start_letter:(start_letter+x)]:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
