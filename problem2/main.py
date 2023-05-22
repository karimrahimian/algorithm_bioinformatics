from Alinger import Aligner

if __name__ == "__main__":
    aligner = Aligner("TCGACGCTACGACG","TCGACGCTACGAC")
    aligner.init_matrix()
    aligner.global_alignment()

    align1, align2, score = aligner.get_score()
    print(align1)
    print(align2)
    print(score)

    aligner = Aligner("TCGACGCTACGACGCGCGCGCGCGCGCGCGCGCGCGCGAC","TCGACGCTACGACAC")
    aligner.init_matrix()
    aligner.global_alignment()

    align1, align2, score = aligner.get_score()
    print(align1)
    print(align2)
    print(score)