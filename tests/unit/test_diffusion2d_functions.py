"""
Tests for functions in class SolveDiffusion2D
"""

from diffusion2d import SolveDiffusion2D
import numpy as np

def test_initialize_domain():
    """
    Check function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    solver.initialize_domain(w=20., h=10., dx=0.2, dy=0.5)
    
    assert type(solver.w) == float
    assert type(solver.h) == float
    assert type(solver.dx) == float
    assert type(solver.dy) == float
    assert type(solver.nx) == int
    assert type(solver.ny) == int

    assert solver.nx == 100
    assert solver.ny == 20

def test_initialize_physical_parameters():
    """
    Checks function SolveDiffusion2D.initialize_domain
    """
    solver = SolveDiffusion2D()
    
    solver.dx = 0.2
    solver.dy = 0.6

    solver.initialize_physical_parameters(D=4.0, T_cold=300.0, T_hot=700.0)

    assert type(solver.D) == float
    assert type(solver.T_cold) == float
    assert type(solver.T_hot) == float
    assert type(solver.dt) == float

def test_set_initial_condition():
    """
    Checks function SolveDiffusion2D.get_initial_function
    """
    solver = SolveDiffusion2D()

    solver.nx = 10
    solver.ny = 20
    solver.dx = 0.4
    solver.dy = 0.2
    solver.T_cold = 300.0
    solver.T_hot = 700.0

    u0 = solver.set_initial_condition()

    assert type(u0) == np.ndarray
    assert solver.nx == u0.shape[0]
    assert solver.ny == u0.shape[1]
