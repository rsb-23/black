import tracemalloc

import black

logfile = open("memory_profile.log", "a")
data_case = "tests/data/"
files = [
    "profiling/mix_big.py",
    f"{data_case}/cases/pep_646.py",
    f"{data_case}/cases/expression.py",
    f"{data_case}/cases/pattern_matching_complex.py",
    f"{data_case}/line_ranges_formatted/pattern_matching.py",
]
files.sort()


def get_mb(x: int) -> str:
    return f"{x / 1024 / 1024 :.3f} MB"


def main() -> None:
    for file in files:
        with open(file) as f:
            code = f.read()
        black.format_str(code, mode=black.FileMode())

    current, peak = tracemalloc.get_traced_memory()
    print(f"Current: {get_mb(current)}; Peak: {get_mb(peak)}", file=logfile)

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("traceback")

    print("[ Top 10 Memory Allocations ]")
    for stat in top_stats[:10]:
        print(stat)


if __name__ == "__main__":
    tracemalloc.start()
    main()
    print("-" * 10, file=logfile)

    tracemalloc.stop()
    logfile.close()
