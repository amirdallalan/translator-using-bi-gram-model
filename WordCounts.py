def WordCounts(doc):
    swc = {}        # single words count
    pwc = {}        # pair word count

    for idx, word in enumerate(doc):
        # number of each word
        if word in swc:
            swc[word] += 1
        else:
            swc[word] = 1

        try:
            if word == "<END>": # skip <END><START> pair count
                continue
            next_word = doc[idx+1] # find next word
        except:
            continue

        # number of each pair word
        if (word, next_word) in pwc:
            pwc[(word, next_word)] += 1
        else:
            pwc[(word, next_word)] = 1
    return swc, pwc