import numpy as np

def BigramProbability(swc, pwc):
  unigram_prob = {}
  for unigram, freq in swc.items():
    unigram_prob[unigram] = freq / np.float64(sum(swc.values()))

  bigram_prob = {}
  for bigram, freq in pwc.items():
      first_word = bigram[0]
      bigram_prob[bigram] = freq / np.float64(swc[first_word])
  return unigram_prob, bigram_prob