import streamlit as st

def levenshtein_distance(source, target):
    m = len(source)
    n = len(target)
    # Create a matrix to store the distances between prefixes.
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize the first row and column of the matrix.
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j

    # Fill in the rest of the matrix.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min( matrix[i - 1][j] + 1,  # deletion
                                matrix[i][j - 1] + 1,  # insertion
                                matrix[i - 1][j - 1] + cost  # substitution
                                )

    # Return the distance between the last prefixes.
    distance = matrix[m][n]
    return distance

def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
vocabs = load_vocab(file_path='./data/vocab.txt')

def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):

        # compute levenshtein distance
        leven_distances = dict()
        for vocab in vocabs:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        
        # sorted by distance
        sorted_distences = dict(sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distences.keys())[0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        
        col2.write('Distances:')
        col2.write(sorted_distences)

if __name__ == "__main__":
    main()
    print(levenshtein_distance("elmets", "elements"))


# Word Correction using Levenshtein Distance
# https://levenshtein-app.streamlit.app/#word-correction-using-levenshtein-distance