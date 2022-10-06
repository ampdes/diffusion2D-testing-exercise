"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np
from unittest import TestCase

class TestSolveDiffusion2D(TestCase):
    """
    Check the class SolveDiffusion2D
    """
    def setUp(self) -> None:
        # parameters for initialize_domain
        self.w=20. 
        self.h=10.
        self.dx=0.2
        self.dy=0.5
        self.nx = 10
        self.ny = 20
        self.T_cold = 300.0
        self.T_hot = 700.0
        self.D = 4.0

    def test_initialize_domain(self):
        """
        Check function SolveDiffusion2D.initialize_domain
        """        
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=self.w, h=self.h, dx=self.dx, dy=self.dy)

        self.assertIsInstance(solver.w, float)
        self.assertIsInstance(solver.h, float)
        self.assertIsInstance(solver.dx, float)
        self.assertIsInstance(solver.dy, float)
        self.assertIsInstance(solver.nx, int)
        self.assertIsInstance(solver.ny, int)

        self.assertEqual(solver.nx, 100)
        self.assertEqual(solver.ny, 20)

    def test_initialize_physical_parameters(self):
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.dx = self.dx
        solver.dy = self.dy

        solver.initialize_physical_parameters(D=self.D, T_cold=self.T_cold, T_hot=self.T_hot)

        self.assertIsInstance(solver.D, float)
        self.assertIsInstance(solver.T_cold, float)
        self.assertIsInstance(solver.T_hot, float)
        self.assertIsInstance(solver.dt, float)

    def test_set_initial_condition(self):
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()

        solver.nx = self.nx
        solver.ny = self.ny
        solver.dx = self.dx
        solver.dy = self.dy
        solver.T_cold = self.T_cold
        solver.T_hot = self.T_hot

        u0 = solver.set_initial_condition()

        self.assertIsInstance(u0, np.ndarray)
        self.assertEqual(solver.nx, u0.shape[0])
        self.assertEqual(solver.ny, u0.shape[1])
