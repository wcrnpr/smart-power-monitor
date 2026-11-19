import numpy as np

def calculate_rms(samples):
    """Calculate AC RMS after removing the mean (DC offset)."""
    data = np.array(samples)      # แปลง list เป็น numpy array
    dc_offset = np.mean(data)
    data = data - dc_offset
    squared = data ** 2            # ขั้น 2: ยกกำลังสองทุกตัว
    mean_val = np.mean(squared)    # ขั้น 3: หาค่าเฉลี่ยทั้งชุด
    rms = np.sqrt(mean_val)        # ขั้น 4: ถอดราก
    return rms


if __name__ == '__main__':
    current_samples = [1.0, 3.0, 1.0, 3.0]  # Example current samples in amperes.
    rms_current = calculate_rms(current_samples)
    print(f"AC RMS current: {rms_current:.4f} A")
