# Build an LLM from Scratch 🧠

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

A hands-on implementation journey following the ["Build a Large Language Model (From Scratch)"](https://github.com/rasbt/LLMs-from-scratch) book by Sebastian Raschka. This repository documents my learning process and practical implementations while building LLM components from the ground up.

## 📖 Overview

This repository contains Python implementations and Jupyter notebooks exploring:
- Transformer architecture components
- Tokenization strategies
- Model training and optimization
- Neural network fundamentals for LLMs
- Text generation techniques

## ✨ Features

- [x] Basic tokenizer implementation
- [x] Transformer block structure
- [ ] Full model architecture
- [ ] Training pipeline
- [ ] Model optimization

## 🚀 Getting Started

### Prerequisites
- Python 3.13
- Jupyter Lab
- pip package manager

### Installation
```bash
# Clone repository
git clone https://github.com/your-username/build-an-llm.git
cd build-an-llm

# Create virtual environment (recommended)
python -m venv llm-env
source llm-env/bin/activate  # Linux/MacOS
# llm-env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Lab
jupyter lab
```

## 📂 Repository Structure
```
.
├── notebooks/          # Jupyter notebooks with implementations
├── src/                # Python modules and utilities
├── data/               # Sample datasets and tokenizers
├── requirements.txt    # Python dependencies
└── LICENSE             # MIT License
```

## 📦 Dependencies
Core packages:
- `torch` (PyTorch)
- `numpy`
- `tqdm`
- `matplotlib`
- `jupyterlab`

Install with:
```bash
pip install -r requirements.txt
```

## 🤝 Contributing
While this is primarily a personal learning project, constructive feedback and suggestions are welcome! Please open an issue first to discuss potential changes.

## 📜 License
Distributed under MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments
- [Sebastian Raschka](https://github.com/rasbt) for the original book and reference implementation
- PyTorch community for excellent documentation
- The open-source ML community for foundational research

## 📚 References
1. ["Build a Large Language Model (From Scratch)"](https://www.manning.com/books/build-a-large-language-model-from-scratch) by Sebastian Raschka
2. [Original Reference Implementation](https://github.com/rasbt/LLMs-from-scratch)

---

> **Note on Python 3.13**  
> Some dependencies might not yet have full support for Python 3.13. If you encounter issues:
> - Use Python 3.12 as fallback
> - Check package versions in `requirements.txt`
> - Report any compatibility issues in the repository