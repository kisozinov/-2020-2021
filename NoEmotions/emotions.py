vocab = dict()
def sq(w):
    out = ' '
    for i in range(len(w) - 1):
        if w[i] != w[i+1]:
            out += w[i]
    if w[-1] != out[-1]:
        out += w[-1]
    return out

f = open("Vocabulary.txt",'r')
vocab_ = f.readlines()

vocab = [i.strip() for i in vocab_]
print(vocab)
vocab_sq = dict.fromkeys([sq(i) for i in vocab])
vocab_sq = {v: [] for v in vocab_sq}
f.close()
for i in vocab:
    #print(i)
    vocab_sq[sq(i)].append(i)
print(vocab_sq)

emotional_word = input()
if vocab_sq.get(sq(emotional_word)) is not None:
    for orig_word in vocab_sq[sq(emotional_word)]:
        #print(i)
        isEqual = True
        i = 0
        emotions_count = 0
        for j in range(len(emotional_word)):

            if i < len(orig_word) - 1 and emotional_word[j] == orig_word[i]:
                i += 1
            elif i >= len(orig_word) - 1 and emotional_word[j] == orig_word[i]:
                if j == i:
                    pass
                else:
                    emotions_count += 1
            else:
                if emotional_word[j] == emotional_word[j - 1]:
                    emotions_count += 1
                else:
                    isEqual = False
                    break
        if len(emotional_word) < len(orig_word):
            isEqual = False
        if len(emotional_word) == len(orig_word) and len(emotional_word) + emotions_count > len(orig_word):
            isEqual = False
        if isEqual:
            print('->' + orig_word)
else:
    print("No such word!")

#print(isEqual)
