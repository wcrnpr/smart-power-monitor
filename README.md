# Smart Power Monitor — NILM Appliance Classification System

ESP32-based Non-Intrusive Load Monitoring (NILM) system that classifies household
appliances from a single point of measurement, using current/voltage sensing and
on-device signal processing — with a TinyML model for real-time classification.

## Status: In Progress (Capstone Project)

This repo documents both the **learning process** (Python → ML → TinyML) and the
**final embedded system**, so the full journey is visible — not just the finished result.

## Tech Stack

- **Hardware:** ESP32 (Arduino/C++), ADS1115 (16-bit ADC, up to 860 SPS), SCT-013-000 (current sensor), ZMPT101B (voltage sensor)
- **Signal processing:** RMS power calculation, FFT-based feature extraction
- **ML/TinyML:** scikit-learn → TensorFlow/Keras → TensorFlow Lite Micro (quantized for on-device inference)
- **Storage/Display:** SD card logging, I2C OLED status display

## Repo Structure

```
smart-power-monitor/
├── notebooks/     — Python/ML learning experiments (RMS, FFT, feature engineering)
├── firmware/      — ESP32 embedded code (Arduino/C++)
└── ml_models/     — Trained models and TFLite Micro conversion
```

## Roadmap

- [x] RMS power calculation from raw current samples (NumPy)
- [ ] FFT-based feature extraction
- [ ] Baseline classifier (scikit-learn: Random Forest / SVM)
- [ ] Neural network classifier (TensorFlow/Keras)
- [ ] Convert to TFLite Micro + quantization
- [ ] Deploy on ESP32
- [ ] Benchmark against published NILM research (IJERT 2026, Springer 2025)

## Background

Built as a capstone project for a Computer Engineering degree (Embedded IoT and
Network track) at Mahanakorn University of Technology, Bangkok.

