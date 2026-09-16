import math
import numpy as np
def manual_mean(values):
    return sum(values) / len(values)
def manual_median(values):
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2
def manual_standard_deviation(values, ddof=0):
    if len(values) <= ddof:
        raise ValueError("Not enough values for the requested standard deviation")
    average = manual_mean(values)
    variance = sum((value - average) ** 2 for value in values) / (len(values) - ddof)
    return math.sqrt(variance)
def main():
    data = np.array([12, 15, 18, 18, 20, 22, 25], dtype=float)
    numpy_mean = np.mean(data)
    numpy_median = np.median(data)
    numpy_std = np.std(data)  # NumPy's default is population standard deviation.
    print(f"Data: {data.tolist()}")
    print(f"Mean: {numpy_mean:.2f} (manual: {manual_mean(data):.2f})")
    print(f"Median: {numpy_median:.2f} (manual: {manual_median(data):.2f})")
    print(
        f"Standard deviation: {numpy_std:.2f} "
        f"(manual: {manual_standard_deviation(data):.2f})"
    )
    print(f"Sample standard deviation (NumPy): {np.std(data, ddof=1):.2f}")
if __name__ == "__main__":
    main()