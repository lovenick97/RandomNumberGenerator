import unittest
import random
from random_generator import RandomGen


class TestRandomGen(unittest.TestCase):

    random_nums = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    def test_random_seed(self):
        """
        Tests shape of distribution is within 5 std of expected distribution
        """

        gen = RandomGen(self.random_nums, self.probabilities)
        n = 100

        # Assume binomial approximation
        expectance = list(map(lambda x: n * x, self.probabilities))
        deviation = list(map(lambda x: ((1-x)*x*n)**0.5, self.probabilities))

        # 5 stds - once in recorded history event
        lcb = [expectance[i] - 5*deviation[i] for i in range(len(expectance))]
        ucb = [expectance[i] + 5*deviation[i] for i in range(len(expectance))]

        results = []
        for i in range(n):
            results.append(gen.next_num())

        for i in range(len(expectance)):
            ct = results.count(self.random_nums[i])
            self.assertGreaterEqual(ucb[i], ct)
            self.assertLessEqual(lcb[i], ct)

    def test_known_seed(self):
        """
        Test case for random seed with known results
        """
        random.seed(153)  # Do not edit

        # First number generated in base case is 3
        gen = RandomGen(self.random_nums, self.probabilities)
        self.assertEqual(gen.next_num(), 3)

        # next 10 numbers in uniform case are correct
        results = []
        for _ in range(10):
            results.append(gen.next_num())
        self.assertEqual(results, [1, 1, 0, 2, 1, 0, 0, 2, 2, 0])

    def test_error_cases(self):

        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3], [])

        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3], [0.1, 0.9])

        with self.assertRaises(TypeError):
            RandomGen([1, 2, 'a'], [0.1, 0.8, 0.1])

        with self.assertRaises(TypeError):
            RandomGen([1, 2, float('inf')], [0.1, 0.8, 0.1])

        with self.assertRaises(TypeError):
            RandomGen([1, 2, 3, 4], [0.1, 0.8, float('nan'), 0.1])

        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3, 4], [0.1, 0.2, 0.3, 0.5])

        with self.assertRaises(ValueError):
            RandomGen([1, 2, 3, 4], [0.1, 0.4, -0.3, 0.8])


if __name__ == "__main__":
    unittest.main()
