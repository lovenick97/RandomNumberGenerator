import random
from warnings import warn


class RandomGen(object):

    _random_nums = [-1, 0, 1, 2, 3]
    _probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    _epsion = 0.0001  # For floating point comparison

    def __init__(self, random_nums: list, probabilities: list) -> None:
        self.random_nums = random_nums
        self.probabilities = probabilities
        self.pdf = dict(zip(random_nums, probabilities))

        self._check_inputs()

    def next_num(self) -> int:
        """
        Returns one of the randomNums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """

        # Generate a random number between 0 and 1
        rand_gen_num = random.random()

        # Sorts inputs in order of decreasing probability
        nums, probs = self._sort_pdf()

        # Convert probabilities to CDF
        probs = self._get_cdf(probs)

        # Retun random number based on CDF
        for num, prob in zip(nums, probs):
            if rand_gen_num - prob < 0:
                return num

    def _sort_pdf(self) -> tuple:
        """
        Returns a tuple of random_nums and their respective probabilities sorted
        from highest probability to lowest probability
        """
        sorted_nums = sorted(self.pdf, key=self.pdf.get, reverse=True)
        sorted_probs = sorted(self.pdf.values(), reverse=True)

        return (sorted_nums, sorted_probs)

    @staticmethod
    def _get_cdf(pdf_values: list) -> list:
        """
        Returns the cumulitive distribution function of pdf_values
        """
        return [sum(pdf_values[:i]) for i in range(1, len(pdf_values) + 1)]

    def _check_inputs(self):
        """
        Basic checks to ensure that the inputs are valid
        """
        if not self.random_nums or not self.probabilities:
            raise ValueError("Inputs cannot be empty lists")

        if not len(self.random_nums) == len(self.probabilities):
            raise ValueError(
                f"List Lengths must be equal. Got {len(self.random_nums)} and {len(self.probabilities)}")

        for _ in (self.random_nums, self.probabilities):
            if not all(isinstance(x, (int, float)) for x in _):
                raise TypeError("Inputs must be a list of integers or floats")

            if any(map(lambda x: True if x == float('inf') else False, _)):
                raise TypeError("Float inf values not allowed")

            if any(map(lambda x: True if x != x else False, _)):
                raise TypeError("Float nan values not allowed")

        if not abs(sum(self.probabilities) - 1) < RandomGen._epsion:
            raise ValueError(
                f"Probabilities must sum to 1. Got {sum(self.probabilities)}")

        if not all([0 <= prob <= 1 for prob in self.probabilities]):
            raise ValueError("Probabilities must be between 0 and 1")

        if not len(set(self.random_nums)) == len(self.random_nums):
            warn("Duplicate values in random_nums")
