import numpy as np

# สมมติว่า current_samples คือ list ของค่าที่อ่านได้จาก SCT-013 (860 ค่า)
current_samples = [...]  # ตัวอย่าง: [0.5, -0.3, 0.8, -0.6, ...]

def calculate_rms(samples):
    data = np.array(samples)      # แปลง list เป็น numpy array
    squared = data ** 2            # ขั้น 2: ยกกำลังสองทุกตัว
    mean_val = np.mean(squared)    # ขั้น 3: หาค่าเฉลี่ยทั้งชุด
    rms = np.sqrt(mean_val)        # ขั้น 4: ถอดราก
    return rms

rms_current = calculate_rms(current_samples)
print(f"RMS Current: {rms_current:.4f} A")
