import unittest
from parameterized import parameterized_class
from typing import List

from sympy import var, pi
from sympy.functions import cos
from calculus_of_variations.isoperimetric_problem import IsoperimetricProblemSolver, t


C1 = IsoperimetricProblemSolver.C1
C2 = IsoperimetricProblemSolver.C2
lambda_0 = IsoperimetricProblemSolver.lambda_0
lambda_1 = var('lambda_1')
lambda_2 = var('lambda_2')


def make_solution(f0: str, t0: float, t1: float, x0: float, x1: float, f_list: List[str], alpha_list: List[float]):
    solution = IsoperimetricProblemSolver(f0, t0, t1, x0, x1, f_list, alpha_list)
    solution.solve(verbose=False)
    return solution


test_case_1 = {
    'solution': make_solution(f0='x_diff ** 2', t0=0, t1=1, x0=0, x1=1, f_list=['x'], alpha_list=[0]),
    'general_solution': C1 + C2 * t + lambda_1 * t ** 2 / (4 * lambda_0),
    'coefficients': {C1: 0, C2: -2, lambda_1 / lambda_0: 12},
    'particular_solution': 3 * t ** 2 - 2 * t,
    'extreme_value': 4,
}
test_case_2 = {
    'solution': make_solution(f0='x_diff ** 2', t0=0, t1=1, x0=0, x1=1, f_list=['t * x'], alpha_list=[0]),
    'general_solution': C1 + C2 * t + lambda_1 * t ** 3 / (12 * lambda_0),
    'coefficients': {C1: 0, C2: -3 / 2, lambda_1 / lambda_0: 30},
    'particular_solution': 5 * t ** 3 / 2 - 3 * t / 2,
    'extreme_value': 6,
}
test_case_3 = {
    'solution': make_solution(f0='x_diff ** 2', t0=0, t1=1, x0=0, x1=0, f_list=['x', 't * x'], alpha_list=[1, 0]),
    'general_solution': C1 + C2 * t + lambda_1 * t ** 2 / (4 * lambda_0) + lambda_2 * t ** 3 / (12 * lambda_0),
    'coefficients': {C1: 0, C2: 36, lambda_1 / lambda_0: -384, lambda_2 / lambda_0: 720},
    'particular_solution': 60 * t ** 3 - 96 * t ** 2 + 36 * t,
    'extreme_value': 192,
}
test_case_4 = {
    'solution': make_solution(f0='x_diff ** 2', t0=0, t1=pi, x0=1, x1=-1, f_list=['x * cos(t)'], alpha_list=[pi / 2]),
    'general_solution': C1 + C2 * t - lambda_1 * cos(t) / (2 * lambda_0),
    'coefficients': {C1: 0, C2: 0, lambda_1/lambda_0: -2},
    'particular_solution': cos(t),
    'extreme_value': pi/2,
}
test_case_5 = {
    'solution': make_solution(f0='t ** 2 * x_diff ** 2', t0=1, t1=2, x0=1, x1=2, f_list=['t * x'], alpha_list=[7 / 3]),
    'general_solution': C1 + C2/t + lambda_1 * t / (4 * lambda_0),
    'coefficients': {C1: 0, C2: 0, lambda_1/lambda_0: 4},
    'particular_solution': t,
    'extreme_value': 7 / 3,
}


@parameterized_class([test_case_1, test_case_2, test_case_3, test_case_4, test_case_5])
class TestSolver(unittest.TestCase):

    def test_general_solution(self):
        self.assertAlmostEqual(self.solution.general_solution, self.general_solution)

    def test_coefficients(self):
        for coef in self.coefficients.keys():
            self.assertAlmostEqual(self.solution.coefficients[coef], self.coefficients[coef])

    def test_particular_solution(self):
        self.assertAlmostEqual(self.solution.particular_solution, self.particular_solution)

    def test_extreme_value(self):
        self.assertAlmostEqual(self.solution.extreme_value, self.extreme_value)


if __name__ == '__main__':
    unittest.main()
