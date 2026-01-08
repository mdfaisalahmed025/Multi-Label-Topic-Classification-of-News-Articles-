
# 📰 MultiLabelNews

MultiLabelNews: Multi-Label Topic Classification of News Articles using BBC News and Guardian Data.  
An end-to-end project to build a **multi-label news classification system**, enabling accurate categorization of articles across multiple topics such as politics, economy, technology, and climate.

---

## Motivation

Modern news articles often cover **multiple overlapping topics**, making it difficult for traditional single-label classifiers to capture the full context. Poor classification limits **content organization, analytics, and recommendation systems**.

This project aims to:

- Automatically assign **multiple relevant topics** to news articles.
- Enable **scalable and accurate news categorization**.
- Facilitate insights for journalists, analysts, and AI-driven news platforms.

Students, researchers, and news platforms can answer questions like:

- Which topics frequently overlap in news coverage?
- How to automatically tag news articles with multiple relevant categories?
- Which models provide the best performance for multi-label classification?

By leveraging **transformer-based models and large-scale datasets**, this project empowers **data-driven news analysis and organization**.

---



## Project Background

**MultiLabelNews** is built on **real-world news data** collected from reputable sources: BBC News and The Guardian. The pipeline includes:

- **Data collection:** Scraping ~97K articles from BBC and The Guardian  
- **Preprocessing:** Cleaning text, encoding labels, handling multi-label annotations  
- **Modeling:** Transformer-based models for multi-label classification  
- **Evaluation:** Analysis of label distributions, overlaps, and classifier performance  
- **Deployment:** ONNX optimization and inference-ready scripts

Key aspects:

- Multi-label classification for **10+ categories**  
- Standardized datasets for reproducible research  
- Modular pipeline for scraping → preprocessing → training → inference  

---


## Project Background

**MultiLabelNews** is built on **real-world news data** collected from reputable sources: BBC News and The Guardian. The pipeline includes:

- **Data collection:** Scraping ~97K articles from BBC and The Guardian and final cleaned data set is 92K
- **Preprocessing:** Cleaning text, encoding labels, handling multi-label annotations  
- **Modeling:** Transformer-based models for multi-label classification  
- **Evaluation:** Analysis of label distributions, overlaps, and classifier performance  
- **Deployment:** ONNX optimization and inference-ready scripts

Key aspects:

- Multi-label classification for **10+ categories**  
- Standardized datasets for reproducible research  
- Modular pipeline for scraping → preprocessing → training → inference  

---



## Project Overview

The system processes news articles and assigns **multiple topic labels** simultaneously.  

### Target Categories (10+)
- Politics  
- Economy  
- Business  
- Technology  
- Health  
- Climate & Environment  
- Science  
- Education  
- Sports  
- Crime & Law  
- International Affairs  
- Society  


## Dataset Validation & Processing

This repository contains the cleaned and processed **multi-label news dataset**, along with the steps taken to ensure **data quality, consistency, and readiness for machine learning**.

### Dataset Validation & Processing Results

- **Initial Dataset:** ~97,000 articles scraped from BBC News and The Guardian  
- **Final Clean Dataset:** ~92,500 articles after preprocessing  
- **Missing Values:** Rows with missing titles, content, or labels were removed  
- **Duplicates:** Removed duplicate articles based on `title` and `description`  
- **Text Cleaning:** Removed HTML tags, special characters, and normalized whitespace  
- **Lowercasing & Tokenization:** Standardized text for NLP models  
- **Weak Labeling / Encoding:** Multi-label target encoding using binary vectors  
- **Train-Test Split:** Dataset split into training, validation, and test sets while maintaining label distributions  

### Data Quality Checks

- **Completeness:** Ensured every article has text content and at least one label  
- **Uniqueness:** Removed duplicates to avoid data leakage in training  
- **Validity:** Checked labels to ensure they match the predefined category list  
- **Consistency:** Standardized category names and multi-label encoding  
- **Integrity:** Ensured no mismatch between article content and associated labels  


### Dataset Columns

| Column Name      | Description                                           | Data Type       |
|------------------|------------------------------------------------------|----------------|
| title            | Title of the news article                             | String         |
| text             | Full content of the article                           | String         |
| labels           | Original multi-label topics associated with article  | List / String  |
| source           | News source (e.g., BBC News, The Guardian)           | String         |
| url              | URL of the original article                            | String         |
| section          | Section of the news website (e.g., Politics, Tech)   | String         |
| revised_labels   | Cleaned & standardized multi-label topics            | List / String  |


---

This **cleaned and processed dataset** is ready for:

- **Transformer-based multi-label classification**  
- **Exploratory Data Analysis (EDA) of topic distributions and overlaps**  
- **Training, validation, and testing of machine learning models**  

> The dataset ensures that all articles are fully labeled, duplicates are removed, and multi-label encoding is consistent for **high-quality model training and evaluation**.



## Training & Model Evaluation

### 🛠️ Model Training

- **Base Model:** `distilroberta-base` transformer encoder  
- **Task:** Multi-label topic classification of news articles  
- **Training Strategy:** Two-stage training with custom data loader  
- **Epochs:** 5 cycles per stage  
- **Accuracy:** Achieved **91% validation accuracy**, demonstrating strong generalization across multiple news topics  
- **Frameworks & Libraries:** PyTorch, Hugging Face Transformers, BLURR  

**Training Workflow:**

1. **Stage 1:** Initial training on full dataset to learn general topic distributions.  
2. **Stage 2:** Fine-tuning on preprocessed and cleaned dataset for higher accuracy and label balance.  
3. **BLURR Inference:** Used BLURR for accelerated inference pipelines, ensuring batch-efficient processing.  
4. **ONNX Conversion:** Exported the trained model to **ONNX** for CPU-optimized inference and deployment.  
5. **Quantization Attempt:** Model quantization failed due to shape inconsistencies; inference continues with full precision ONNX models.

---



### 📊 Model Benchmarking

| Model Stage        | Base Architecture     | Validation Accuracy | Epochs | Remarks                                  |
|------------------- |-------------------- |------------------ |------- |---------------------------------------- |
| **Stage 1**        | distilroberta-base  | 90%              | 10     | Initial training on raw preprocessed data |
| **Stage 2**        | distilroberta-base  | **91%**           | 10     | Fine-tuned for label balance and noise reduction |

✅ **Conclusion:**  
- Two-stage training with DistilRoBERTa achieved high performance with 91% validation accuracy.  
- BLURR inference ensures efficient prediction on batches of articles.  
- ONNX export provides deployment-ready models, though quantization was not feasible due to shape inconsistencies.

---

### 🔍 Evaluation & Metrics

- **Metric:** Multi-label F1-score, Precision, and Recall were used to assess model performance across all topic labels  
- **Confusion Analysis:** Observed model accurately predicts multiple overlapping topics such as *Politics + Economy* or *Technology + Science*  
- **Label-wise Performance:** Best performance on high-frequency labels (Politics, Economy), slightly lower recall on niche categories (Climate & Environment, Society)  

<p align="center">
  <img src="/screenshots/learning rate.png" width="650" height="450" alt="Multi-Label Confusion Matrix"/>
</p>

✅ **Interpretation:**  
- Diagonal blocks indicate correct multi-label predictions.  
- Off-diagonal misclassifications show overlapping topic predictions where articles belong to multiple categories.  
- Overall, the model demonstrates strong predictive power for multi-label classification tasks.

---

### ⚡ Deployment & Inference

- **BLURR Inference Pipelines:** Fast batch predictions with tokenized inputs  
- **ONNX Models:** Optimized for CPU inference; ready for API integration  
- **Quantization Limitation:** Unable to quantize due to shape mismatch; models still perform efficiently in full precision  






















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
