# 📰 Multi-Label Topic Classification of News Articles

An **end-to-end machine learning pipeline** for multi-label topic classification of news articles, covering data collection, preprocessing, training, ONNX optimization, and deployment-ready inference.  
This project is designed for **research, production, and deployment**, with large trained models stored externally for efficiency.

---

## 🚀 Project Highlights
- 🔖 **Multi-label text classification** (one article → multiple topics)  
- 🧠 **Transformer-based architecture**  
- ⚡ **Optimized ONNX inference** for CPU  
- 🧩 **Modular pipeline**: scraping → training → inference  
- 🌐 **Deployment-ready** (Hugging Face / API friendly)  
- 📦 **Large models stored externally** (GitHub-safe)

---

## 📁 Project Structure


Multi-Label-Topic-Classification-of-News-Articles/
│
├── data/ # Raw & processed datasets
├── dataloaders/ # Data loaders & preprocessing artifacts
├── labeling/ # Label encoding & mappings
├── models/ # (Ignored) trained models
├── notebooks/ # Experiments & analysis notebooks
├── pipeline/ # Training & inference pipelines
├── scraper/ # News scraping utilities
├── website_deployment/ # Web / API deployment code
├── huggingface_deployment/ # HF-compatible inference setup
│
├── config.py # Central configuration
├── requirements.txt # Dependencies
├── test.py # Inference testing
├── README.md # Project documentation
└── .gitignore # Git ignore rules



---

## 🧠 Model Architecture

- **Base Model:** Transformer-based encoder  
- **Task:** Multi-label classification  
- **Output:** Binary relevance per topic  
- **Inference format:** ONNX (CPU-optimized)  

---

## 📥 Download Trained Models (Required)

Due to GitHub file size limits, **trained models are hosted externally**.  

| Model Type | Description | Download Link |
|------------|-------------|---------------|
| Final ONNX Model | Optimized CPU inference | [Download](https://drive.google.com/file/d/1fuhW4hpIsLmlKlwadirXNzquwU3F5Xxw/view) |
| Final PyTorch / Pickle Model | Full training weights | [Download](https://drive.google.com/file/d/1rILhNxyiOb8LnWiJbsRVwyVpnokjIBIf/view) |
| Stage / Backup Model | Backup / intermediate version | [Download](https://drive.google.com/file/d/1vwKPcRc28kgrJ_jS6MDkNyNx6eE6NEtd/view) |

---

## ⚙️ Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/mdfaisalahmed025/Multi-Label-Topic-Classification-of-News-Articles-.git
cd Multi-Label-Topic-Classification-of-News-Articles-



---

If you want, I can also **make a visually richer README with badges, table of contents, and black/white premium theme style** that looks like a **professional GitHub project**.  

Do you want me to do that next?
