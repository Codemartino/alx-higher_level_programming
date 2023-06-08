#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    leng = len(sys.argv)
    sum = 0
    for k in range(leng):
        if k == 0:
            continue
        sum += int(sys.arg [k])
    print('{}'.format(sum))
