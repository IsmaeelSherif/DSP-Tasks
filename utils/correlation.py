from collections import deque as dq
import numpy as np


def correlation(magnitudes_1,magnitudes_2,periodic):
    N = len(magnitudes_1)
    results = []
    signal_2 = dq(magnitudes_2)
    if periodic:
        squared_sum_1 = sum(x*x for x in magnitudes_1)
        squared_sum_2 = sum(x*x for x in magnitudes_2)
        root = np.sqrt(squared_sum_1 * squared_sum_2)
        normalization_factor = round(root / N,2)
        for i in range(N):
            result = 0
            for j in range(N):
                result += magnitudes_1[j]*signal_2[j]
            result /= N
            result = round(result,2)
            result /= normalization_factor
            results.append(round(result,2))
            signal_2.rotate(-1)

    else:
        for i in range(N):
            result = 0
            normalization_factor =round( np.sqrt(sum(x*x for x in magnitudes_1)*sum(x*x for x in magnitudes_2))/N,2)
            print(normalization_factor)
            for j in range(N):
                result += magnitudes_1[j]*signal_2[j]
            result /= N
            result = round(result,2)
            result /= normalization_factor
            results.append(round(result,2))
            signal_2.rotate(-1)
            signal_2[-1] = 0
    return results
