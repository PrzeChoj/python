"""
SPOJ 1145
Czy zostana jakies cukierki po rozdaniu?
"""
D = int(input())
for d in range(D):
    s = input()
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = int(s[i])


    while s[0] >= s[1]:
        s[0] -= s[1]

    if s[0] == 0:
        print("NIE")
    else:
        print("TAK")