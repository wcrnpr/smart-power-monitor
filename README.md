# AI Smart Power Monitoring

A personal engineering portfolio project for non-intrusive load monitoring (NILM)
and motor condition monitoring. The goal is to classify household appliances
from a single measurement point and track motor health using sensor signals,
signal processing, and TinyML on an ESP32-S3.

## Project status

The project is in progress. The repository currently contains Python experiments
for AC RMS current and basic data analysis.

## Tech Stack

- **Hardware:** ESP32-S3 (Arduino/C++), ADS1115 (16-bit ADC, up to 860 SPS), SCT-013-000 (current sensor), ZMPT101B (voltage sensor)
- **Signal processing:** AC RMS current calculation, FFT-based feature extraction
- **ML/TinyML:** scikit-learn → TensorFlow/Keras → TensorFlow Lite Micro (quantized for on-device inference)
- **Storage/Display:** SD card logging, I2C OLED status display

## Repo Structure

```
smart-power-monitor/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── README.md
├── docs/
│   └── README.md
├── firmware/
│   └── README.md
├── ml/
│   └── README.md
├── notebooks/
│   ├── 02_pandas_data_analysis.py
│   └── rms_calculation.py
└── tests/
    └── README.md
```

## Run the AC RMS example

With the Python dependencies listed in `requirements.txt` available, run this from the repository root.

```sh
python notebooks/rms_calculation.py
```

The example removes the DC offset and prints `AC RMS current: 1.0000 A`.

## Roadmap

- [x] AC RMS current calculation from samples in amperes (NumPy)
- [ ] FFT-based feature extraction
- [ ] Baseline classifier (scikit-learn: Random Forest / SVM)
- [ ] Neural network classifier (TensorFlow/Keras)
- [ ] Convert to TFLite Micro + quantization
- [ ] Deploy on ESP32-S3
- [ ] Define motor condition targets and collect baseline measurements
- [ ] Benchmark against published NILM research (IJERT 2026, Springer 2025)

