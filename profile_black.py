import tracemalloc

import black

tracemalloc.start()

data_case = "tests/data/cases"
files = ("profiling/mix_big.py", f"{data_case}/pep_646.py",
         f"{data_case}/expression.py")
for file in files:
    with open(file) as f:
        code = f.read()
    # breakpoint()
    result = black.format_str(code, mode=black.FileMode())

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

print("[ Top 10 Memory Allocations ]")
for stat in top_stats[:10]:
    print(stat)

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB; Peak: {peak / 1024 / 1024:.2f} MB")
tracemalloc.stop()
