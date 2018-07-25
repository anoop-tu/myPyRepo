s = 'I am a good boy'
N = 300
L = len(s)
#print(len1)
words = list(s.split())
W = len(words)
#print(words)
if N < L:
    C = s.count(s[N])
else:
    C = s.count(s[L-1])

print(N,L,C,W)

if C > W:
    words.pop()
else:
    words.pop(C-1)
#print(words)
print(' '.join(word for word in words))
