import numpy as np
class Aligner():
    def __init__(self,seq1,seq2):
        self.seq1 = seq1
        self.seq2 = seq2
        self.match_reward = 1
        self.gap_penalty = -1
        self.mismatch_penalty = -1
    def init_matrix(self):
        n = len(self.seq1)
        m = len(self.seq2)
        self.score = np.zeros((n+1,m+1))
        for i in range(1, n + 1):
            self.score[i][0] = self.gap_penalty * i
        for j in range(1, m + 1):
            self.score[0][j] = self.gap_penalty * j
    def global_alignment(self):
        n = len(self.seq1)
        m = len(self.seq2)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                match_score = self.score[i - 1][j - 1] + (self.match_reward if self.seq1[i - 1] == self.seq2[j - 1] else self.mismatch_penalty)
                delete_score = self.score[i - 1][j] + self.gap_penalty
                insert_score = self.score[i][j - 1] + self.gap_penalty
                self.score[i][j] = max(match_score, delete_score, insert_score)
    def get_score(self):
        align1 = ""
        align2 = ""
        n = len(self.seq1)
        m = len(self.seq2)
        i = n
        j = m
        while i > 0 or j > 0:
            if i > 0 and j > 0 and self.score[i][j] == self.score[i - 1][j - 1] + (
            self.match_reward if self.seq1[i - 1] == self.seq2[j - 1] else self.mismatch_penalty):
                align1 = self.seq1[i - 1] + align1
                align2 = self.seq2[j - 1] + align2
                i -= 1
                j -= 1
            elif i > 0 and self.score[i][j] == self.score[i - 1][j] + self.gap_penalty:
                align1 = self.seq1[i - 1] + align1
                align2 = "-" + align2
                i -= 1
            else:
                align1 = "-" + align1
                align2 = self.seq2[j - 1] + align2
                j -= 1
        return (align1, align2, self.score[n][m])