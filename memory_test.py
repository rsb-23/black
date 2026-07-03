import pathlib
import tracemalloc

import black

tracemalloc.start()

code = pathlib.Path("profiling/mix_big.py").read_text()
result = black.format_str(code, mode=black.FileMode())

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB; Peak: {peak / 1024 / 1024:.2f} MB")
tracemalloc.stop()
