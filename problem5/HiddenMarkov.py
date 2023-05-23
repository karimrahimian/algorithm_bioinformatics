import numpy as np
class HMM():
    def __init__(self):
        pass
    def Viterbi(self,observation, transitionMatrix, emissionMatrix):
        T = len(observation)
        N = transitionMatrix.shape[0]

        viterbiMatrix = np.zeros((N, T))
        path = np.zeros((N, T), dtype=int)

        for t in range(1, T):
            for j in range(N):
                max_prob = -np.inf
                max_path = 0
                for i in range(N):
                    prob = viterbiMatrix[i, t-1] + np.log(transitionMatrix[i, j]) +np.log(emissionMatrix[j, observation[t]])
                    if prob > max_prob:
                        max_prob = prob
                        max_path = i
                viterbiMatrix[j, t] = max_prob
                path[j, t] = max_path

        max_prob = -np.inf
        max_path = 0
        for i in range(N):
            if viterbiMatrix[i, T-1] > max_prob:
                max_prob = viterbiMatrix[i, T-1]
                max_path = i
        hiddenStates = np.zeros(T, dtype=int)
        hiddenStates[-1] = max_path
        for t in range(T-2, -1, -1):
            hiddenStates[t] = path[hiddenStates[t+1], t+1]

        return hiddenStates

    def ForwardAlgorithm(self,observations, states, startProb, transitionMatrix, emissionMatrix):
        n = len(observations)
        m = len(states)
        # Initialize  probabilities
        forward_probs = [[0] * m for i in range(n)]
        for i, state in enumerate(states):
            forward_probs[0][i] = startProb[i] * emissionMatrix[i][observations[0]]
        for t in range(1, n):
            for j, state in enumerate(states):
                forward_probs[t][j] = emissionMatrix[j][observations[t]] * sum(
                    forward_probs[t - 1][i] * transitionMatrix[j][j] for i in range(m))

        p = sum(forward_probs[n - 1][j] for j in range(m))

        return p