import numpy as np

def calculate_rms(samples):
    """Calculate AC RMS after removing the mean (DC offset)."""
    data = np.array(samples)      # Convert the sample list to a NumPy array.
    dc_offset = np.mean(data)
    data = data - dc_offset
    squared = data ** 2            # Square each mean-centered sample.
    mean_val = np.mean(squared)    # Calculate the mean of the squared samples.
    rms = np.sqrt(mean_val)        # Take the square root of the mean.
    return rms


if __name__ == '__main__':
    current_samples = [1.0, 3.0, 1.0, 3.0]  # Example current samples in amperes.
    rms_current = calculate_rms(current_samples)
    print(f"AC RMS current: {rms_current:.4f} A")
