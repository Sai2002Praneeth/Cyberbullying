# Cyberbullying Detection using NLP 💬

This project focuses on detecting and blocking bullying content in social media posts and comments using machine learning and natural language processing (NLP) techniques. Built with a **Gradio** web interface, it provides real-time monitoring to help prevent the spread of harmful content.

## Live Demo 🚀

You can try the live application hosted on Hugging Face Spaces:

**➡️ [Try the Live App Here!](https://huggingface.co/spaces/Codeszz/Cyberbullying)**

---

## Table of Contents
1.  [Overview](#overview)
2.  [Features](#features)
3.  [Installation](#installation)
4.  [Usage](#usage)
5.  [Model and Approach](#model-and-approach)

---

## Overview ℹ️

Cyberbullying on social media can have a significant impact on mental health. This project aims to create a safer online environment by identifying bullying content in real-time and blocking it before it reaches users. The application uses a trained machine learning model to classify content and alert moderators when bullying is detected.

---

## Features ✨

* **Real-time Detection**: Automatically detects bullying content in posts and comments.
* **NLP-based Analysis**: Uses natural language processing to analyze the tone and intent of content.
* **Simple Interface**: Easy-to-use web interface for quick checks.

---

## Installation 🛠️

To run the project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Sai2002Praneeth/cyberbullying-app.git](https://github.com/Sai2002Praneeth/cyberbullying-app.git)
    cd cyberbullying-app
    ```

2.  **Create and activate a virtual environment (for Windows):**
    ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Gradio application:**
    ```bash
    python app.py
    ```

5.  Open the application in your browser at **`http://127.0.0.1:7860`**.

---

## Usage 📝

1.  Open the application in your browser.
2.  Enter the social media post or comment text in the provided input field.
3.  Click on **Submit**. The model will classify the content.
4.  The result ("Bullying" or "Non-Bullying") will be displayed in the output box.

---

## Model and Approach 🤖

The model was developed using machine learning and NLP techniques to analyze social media content. Key steps included:

* **Data Collection**: We compiled a dataset of over 40,000 social media posts and comments with labeled bullying content.
* **Preprocessing**: Text data was cleaned, tokenized, lemmatized, and stop words were removed.
* **Feature Extraction**: We extracted relevant features using the **TF-IDF** (Term Frequency-Inverse Document Frequency) technique.
* **Model Training**: Multiple classifiers were tested. The final model chosen was the **Stochastic Gradient Descent (SGD) Classifier**, which achieved an **accuracy of 87%** on the test set.

---
## Analysis Repository 🔬

The full development process, including data exploration and model comparison, can be found in the **[cyberbullying-analysis repository](https://github.com/Sai2002Praneeth/cyberbullying-analysis)**.
