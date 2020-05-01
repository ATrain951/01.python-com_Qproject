def count_substring(string, sub_string):
    return sum([string[i:i + len(sub_string)] == sub_string for i in range(len(string) - len(sub_string) + 1)])


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
