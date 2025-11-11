# verify_imports.py
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import datasets
    print("All libraries imported successfully!")
    
    # Additional verification
    print(f"NumPy array: {np.array([1, 2, 3])}")
    print(f"Pandas version: {pd.__version__}")
    
except ImportError as e:
    print(f"Import error: {e}")
