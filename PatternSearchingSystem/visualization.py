import matplotlib.pyplot as plt


def plot_execution_time(results):
    algorithms = list(results.keys())
    times = [results[algo]["time"] for algo in algorithms]

    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, times)

    plt.xlabel("Algorithms")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Execution Time Comparison")

    plt.show()


def plot_match_count(results):
    algorithms = list(results.keys())
    matches = [len(results[algo]["positions"]) for algo in algorithms]

    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, matches)

    plt.xlabel("Algorithms")
    plt.ylabel("Matches Found")
    plt.title("Pattern Match Comparison")

    plt.show()


def plot_comparisons(results):
    algorithms = list(results.keys())
    comparisons = [results[algo]["comparisons"] for algo in algorithms]

    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, comparisons)

    plt.xlabel("Algorithms")
    plt.ylabel("Comparisons")
    plt.title("Comparison Count Analysis")

    plt.show()