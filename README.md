# Translator using Bi-gram Model

This project is an educational implementation of a language translator based on a bi-gram model, which utilizes probabilistic word pairs for translation from Persian to English. The translator leverages the Reuters dataset for creating bigrams and uses the `GoogleTranslator` API to initially translate input words before applying bigram probabilities. Note that this project is built as an instructional example, and it may not achieve high translation accuracy.

## Project Overview

The project consists of the following main steps:

1. **Dataset Preparation**: 
   - Load the Reuters corpus to analyze and create bi-gram probabilities.
   - Tokenize, stem, and filter the text data by removing common stop words.

2. **Bigram Model Construction**:
   - Compute unigram and bigram counts to form probabilities.
   - Calculate likelihoods based on these probabilities to predict word pairs.

3. **Translation Process**:
   - Input Persian sentences are normalized, tokenized, and translated word-by-word using `GoogleTranslator`.
   - Use the bi-gram model to reorder words based on calculated probabilities.

4. **Permutation and Probability Calculation**:
   - Generate permutations of possible translations and calculate their probabilities using the trained bigram model.
   - Select the most probable permutation as the final translation.

## Getting Started

To use this project, follow these steps:

1. Clone this repository.
2. Install the required Python packages:
   ```bash
   pip install nltk pandas numpy hazm matplotlib deep-translator
3. Run the script to see the translation process for a sample Persian input sentence.

## Dependencies

    Python 3.7+
    Required packages: nltk, pandas, numpy, hazm, matplotlib, deep-translator

## Note

This translator is a proof-of-concept and is intended for learning purposes only. It may not perform accurate translations due to the limitations of the bi-gram model and the simplistic approach used.

## License

This project is open-source and available under the MIT License.

## Acknowledgments
This project uses the Reuters dataset from the NLTK library and the Google Translator API for initial translations.

