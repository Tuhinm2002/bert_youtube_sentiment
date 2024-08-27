# 🎥 Realtime YouTube Sentiment Analysis Using BERT and YouTube API 🤖

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Docker Hub](https://img.shields.io/badge/Docker-Hub-blue?logo=docker)](https://hub.docker.com/r/your-dockerhub-username/your-repo-name)
[![GitHub Stars](https://img.shields.io/github/stars/tuhinm2002/bert_youtube_sentiment.svg?style=social)](https://github.com/Tuhinm2002/bert_youtube_sentiment)

## 📖 Overview

This project leverages the power of **BERT** (Bidirectional Encoder Representations from Transformers) and the **YouTube Data API** to perform real-time sentiment analysis on YouTube comments. The tool fetches comments from any YouTube video and categorizes them as **positive** or **negative** in real-time.

## ✨ Key Features

- ⚡ **Real-Time Analysis:** Analyze YouTube comments in real-time using a fine-tuned BERT model.
- 🎥 **YouTube API Integration:** Seamlessly integrates with the YouTube Data API to fetch video comments.
- 🐳 **Dockerized Deployment:** Easily deploy the project using Docker.
- 🤗 **Hugging Face Integration:** Leverages Hugging Face's Transformers library for model inference.

## 🗂️ Table of Contents

- [📥 Installation](#-installation)
- [🚀 Usage](#-usage)
- [🛠️ Project Structure](#️-project-structure)
- [🧠 Model Details](#-model-details)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 📥 Installation

### Prerequisites

- 🐍 Python 3.8 or higher
- 🐳 Docker
- 🔑 YouTube Data API Key

### Clone the Repository

```bash
git clone https://github.com/your-username/realtime-youtube-sentiment.git
cd realtime-youtube-sentiment
pip install -r requirements.txt
```
## 🧠 Model Details

This project uses a fine-tuned **BERT** model trained on a large dataset of Twitter comments. The model is optimized for binary sentiment classification and is capable of accurately distinguishing between positive and negative sentiments.

The model architecture is as follows:
- **Base Model:** BERT (Bidirectional Encoder Representations from Transformers)
- **Pre-training:** General English text corpus
- **Fine-tuning:** Twitter sentiment dataset with binary labels (positive/negative)

The BERT model leverages the Transformer architecture to understand the context of comments and provides a real-time sentiment prediction.

## 🤝 Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, feel free to fork this repository and submit a pull request. Here’s how you can contribute:

1. **Fork the Repository**: Click on the 'Fork' button at the top of this repository.
2. **Create a New Branch**: Create a branch for your feature or bugfix (`git checkout -b feature-name`).
3. **Commit Your Changes**: Commit your changes to your branch (`git commit -m 'Add feature'`).
4. **Push to the Branch**: Push your changes to your branch (`git push origin feature-name`).
5. **Create a Pull Request**: Open a pull request in the repository.

Thank you for contributing! 🙌

## 📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute this software in accordance with the license. See the [LICENSE](LICENSE) file for more details.

---

**MIT License**
