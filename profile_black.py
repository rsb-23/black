import tracemalloc
from pathlib import Path

import black

tracemalloc.start()

# Run black on a directory
# src = Path("/src")
# mode = black.FileMode()
# list(black.reformat_many(src, fast=False, mode=mode, write_back=black.WriteBack.YES))

code = Path("profiling/mix_big.py").read_text()
result = black.format_str(code, mode=black.FileMode())

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 Memory Allocations ]")
for stat in top_stats[:10]:
    print(stat)

current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB; Peak: {peak / 1024 / 1024:.2f} MB")
tracemalloc.stop()
