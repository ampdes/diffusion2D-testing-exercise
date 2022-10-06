#!/usr/bin/bash

# Run the pytest 
python3 -m pytest >> pytest.log

# Run the unittests with unittest framework
python3 -m unittest tests/unit/test_diffusion2d_functions.py >> unittest.log

# Run the script

python3 diffusion2d.py


