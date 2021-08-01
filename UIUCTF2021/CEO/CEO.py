from itertools import permutations

common_words = []
num_words_in_pw = 2


with open('3000+ Common English Words.txt', 'r') as f:
    for line in f.readlines():
        common_words.append(line[:-1])


def write_flag(f, perm):
    flag = ''
    for word in perm:
        flag += word + '_'
    flag = flag[:-1] + '\n'
    f.write(flag)


with open('dictionary' + str(num_words_in_pw) + '.txt', 'w') as f:
    perms = permutations(common_words[3:], num_words_in_pw)
    for perm in perms:
        write_flag(f, perm)


