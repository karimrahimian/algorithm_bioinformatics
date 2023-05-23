from HiddenMarkov import HMM
import numpy as np

if __name__ == "__main__":
    hmm = HMM()
    states = ['Sunny','Cloudy','Rainy']
    observation = [1, 2, 2]
    transitionMatrix = np.array([[0.7, 0.2, 0.1 ],
                                 [0.3,0.5,0.2],
                                 [0.2,0.4,0.4]])
    emissionMatrix = np.array([[0.4, 0.4, 0.2],
                               [0.2, 0.6,0.2],
                               [0.1,0.3,0.6]])

    hiddenStates = hmm.Viterbi(observation, transitionMatrix, emissionMatrix)

    print("Most likely sequence of hidden states:", hiddenStates)

    observations = [1, 2, 2]
    transitionMatrix = np.array([[0.7, 0.2, 0.1 ],
                                 [0.3,0.5,0.2],
                                 [0.2,0.4,0.4]])
    emissionMatrix = np.array([[0.4, 0.4, 0.2],
                               [0.2, 0.6,0.2],
                               [0.1,0.3,0.6]])
    states = ['Sunny', 'Cloudy', 'Rainy']
    startProb = [0,1,1]

    hiddenStates = hmm.ForwardAlgorithm(observations, states, startProb, transitionMatrix, emissionMatrix)

    print("Most likely path of using forward algorithm:", hiddenStates)