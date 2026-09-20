
# time O(n^2) ???
# space O(1)


def count_substring(string, sub_string):
    lenss = len(sub_string)
    count = 0
    for i in range((len(string) - lenss) + 1):
        if string[i: i + lenss] == sub_string:
            count += 1
    return count


if __name__ == '__main__':
    string = 'ABCDCDC'
    sub_string = 'CDC'

    count = count_substring(string, sub_string)
    print(count)
