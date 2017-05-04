def count_as(s):
    count_a = 0
    count_ae = 0
    count_aei = 0
    count_aeio = 0
    count_aeiou = 0
    for letter in s:
        if letter == 'a':
            count_a+=1
        elif letter == 'e' and count_a > 0:
            count_ae = max(count_ae,count_a) + 1
        elif letter == 'i' and count_ae > 0:
            count_aei = max(count_aei,count_ae) + 1
        elif letter == 'o' and count_aei > 0:
            count_aeio = max(count_aeio,count_aei) + 1
        elif letter == 'u' and count_aeio > 0:
            count_aeiou = max(count_aeiou,count_aeio) + 1
    return count_ae

def Main():
    s = 'aeaeaeaeae'
    print(count_as(s))


if __name__ == '__main__':
    Main()


