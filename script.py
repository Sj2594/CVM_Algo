import random
import math

class CVM:
    def __init__(self, epsilon, delta):
        self.epsilon = epsilon
        self.delta = delta
        self.hashes = []

    def hash_function(self, x):
        random.seed(x)
        return random.random()

    def estimate(self, data):
        n = len(data)
        k = math.ceil((1 / self.epsilon) ** 2 * math.log(1 / self.delta))
        self.hashes = [self.hash_function(x) for x in data]
        self.hashes.sort()
        return k / self.hashes[k - 1]

# Example usage
data = [1, 2, 2, 3, 8, 11, 4, 45]
cvm = CVM(epsilon=0.01, delta=0.001)
estimate = cvm.estimate(data)
print(f"Estimated number of unique elements: {estimate}")
