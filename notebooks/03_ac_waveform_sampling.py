"""Engineering Lab 01: Sample a sinusoidal current and compare RMS values."""

import matplotlib.pyplot as plt
import numpy as np


def calculate_rms(samples):
    """Return the root mean square of the supplied current samples."""
    return np.sqrt(np.mean(np.square(samples)))


def main():
    """Generate the samples, report the RMS comparison, and display the plot."""
    frequency_hz = 50.0
    peak_current_a = 2.0
    sampling_rate_hz = 1000.0
    duration_s = 0.1
    sample_count = round(sampling_rate_hz * duration_s)
    sampling_interval_s = 1.0 / sampling_rate_hz

    time_s = np.linspace(0.0, duration_s, sample_count, endpoint=False)
    current_a = peak_current_a * np.sin(2.0 * np.pi * frequency_hz * time_s)

    total_rms_a = calculate_rms(current_a)
    ac_rms_a = calculate_rms(current_a - np.mean(current_a))
    theoretical_rms_a = peak_current_a / np.sqrt(2.0)

    print(f"Sampling interval: {sampling_interval_s:.6f} s")
    print(f"Sample count: {sample_count}")
    print(f"Total RMS current: {total_rms_a:.4f} A")
    print(f"AC-only RMS current: {ac_rms_a:.4f} A")
    print(f"Theoretical RMS current: {theoretical_rms_a:.4f} A")
    print(f"Absolute difference (total vs. theoretical): {abs(total_rms_a - theoretical_rms_a):.3e} A")

    _, axes = plt.subplots()
    axes.plot(time_s, current_a, marker=".")
    axes.set(xlabel="Time (s)", ylabel="Current (A)", title="Sampled 50 Hz AC Current")
    axes.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
