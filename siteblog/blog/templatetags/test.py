s = 'Koshka'


def reverse_string(s_in = '111'):
    if len(s_in) == 1:
        return s_in
    else:
        return s_in[-1]+reverse_string(s_in[:-1])


print(reverse_string(s))
