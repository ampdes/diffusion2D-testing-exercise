# Python code to solve the diffusion equation in 2D

Please follow the instructions in [python_testing_exercise.md](https://github.com/RSE-102/Lecture-Material/blob/main/04_testing/python_testing_exercise.md).

## Test logs (for submission)

### pytest log

Failing *unittest* for `initialize_domain` :


```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/ampdes/mystorage/rse/rse102/diffusion2D-testing-exercise
plugins: anyio-3.4.0, xonsh-0.9.13
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py F..                             [100%]

=================================== FAILURES ===================================
____________________________ test_initialize_domain ____________________________

    def test_initialize_domain():
        """
        Check function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
        solver.initialize_domain(w=20., h=20., dx=0.2, dy=0.5)
    
        assert type(solver.w) == float
        assert type(solver.h) == float
        assert type(solver.dx) == float
        assert type(solver.dy) == float
        assert type(solver.nx) == int
        assert type(solver.ny) == int
    
        assert solver.nx == 100
>       assert solver.ny == 20
E       assert 40 == 20
E        +  where 40 = <diffusion2d.SolveDiffusion2D object at 0x7f52141c5b20>.ny

tests/unit/test_diffusion2d_functions.py:23: AssertionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_domain - ass...
========================= 1 failed, 4 passed in 0.43s ==========================
```

Failing *unittest* from `initialize_physical_parameters`:

```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/ampdes/mystorage/rse/rse102/diffusion2D-testing-exercise
plugins: anyio-3.4.0, xonsh-0.9.13
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py .F.                             [100%]

=================================== FAILURES ===================================
_____________________ test_initialize_physical_parameters ______________________

    def test_initialize_physical_parameters():
        """
        Checks function SolveDiffusion2D.initialize_domain
        """
        solver = SolveDiffusion2D()
    
        solver.dx = 0.2
        solver.dy = 0.6
    
>       solver.initialize_physical_parameters(D=0., T_cold=300.0, T_hot=700.0)

tests/unit/test_diffusion2d_functions.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x7fd138fa75b0>, D = 0.0
T_cold = 300.0, T_hot = 700.0

    def initialize_physical_parameters(self, D=4., T_cold=300.0, T_hot=700.0):
        self.D = D
        self.T_cold = T_cold
        self.T_hot = T_hot
    
        # Computing a stable time step
        dx2, dy2 = self.dx * self.dx, self.dy * self.dy
>       self.dt = dx2 * dy2 / (2 * self.D * (dx2 + dy2))
E       ZeroDivisionError: float division by zero

diffusion2d.py:55: ZeroDivisionError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_initialize_physical_parameters
========================= 1 failed, 4 passed in 0.44s ==========================
```

Failing *unittest* for `set_initial_condition`:

```
============================= test session starts ==============================
platform linux -- Python 3.8.10, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/ampdes/mystorage/rse/rse102/diffusion2D-testing-exercise
plugins: anyio-3.4.0, xonsh-0.9.13
collected 5 items

tests/integration/test_diffusion2d.py ..                                 [ 40%]
tests/unit/test_diffusion2d_functions.py ..F                             [100%]

=================================== FAILURES ===================================
__________________________ test_set_initial_condition __________________________

    def test_set_initial_condition():
        """
        Checks function SolveDiffusion2D.get_initial_function
        """
        solver = SolveDiffusion2D()
    
        solver.nx = 10
        solver.ny = 20
        solver.dx = 0.4
        solver.dy = 0.2
        solver.T_hot = 700.0
    
>       u0 = solver.set_initial_condition()

tests/unit/test_diffusion2d_functions.py:53: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <diffusion2d.SolveDiffusion2D object at 0x7f4018a233a0>

    def set_initial_condition(self):
>       u = self.T_cold * np.ones((self.nx, self.ny))
E       TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'

diffusion2d.py:60: TypeError
=========================== short test summary info ============================
FAILED tests/unit/test_diffusion2d_functions.py::test_set_initial_condition
========================= 1 failed, 4 passed in 0.45s ==========================
```
### unittest log

## Citing

The code used in this exercise is based on [Chapter 7 of the book "Learning Scientific Programming with Python"](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/).
