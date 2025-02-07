# 🔍 Visual Search Engine using VLMs

A deep learning-based **Visual Search Engine** that retrieves similar images using **Vision-Language Models (VLMs)**.  
Supports **image & text-based search**, AI-powered **feature extraction (ResNet-18)**, and an interactive **Streamlit UI** for fast, efficient retrieval.

## 📌 Features
- ✅ **Image-based search** – Find visually similar images from a dataset  
- ✅ **Text-based search** – Retrieve images using keywords or descriptions  
- ✅ **Deep Learning-powered feature extraction** – Uses **ResNet-18**  
- ✅ **Fast similarity search** with precomputed embeddings  
- ✅ **Streamlit UI** – User-friendly, interactive interface  

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Krishnandu-Halder/Visual_Search_Engine_using_VLM.git
cd Visual_Search_Engine_using_VLM
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

python feature_extraction.py

streamlit run app.py

python search.py --query path/to/query_image.jpg

python search.py --text "A cat sitting on a chair"



📂 Visual_Search_Engine_using_VLM
│── 📂 images/              # Dataset of images  
│── 📂 models/              # Pre-trained model storage  
│── 📜 app.py               # Streamlit UI application  
│── 📜 feature_extraction.py  # Extracts image feature vectors  
│── 📜 search.py            # CLI for searching images  
│── 📜 requirements.txt      # Required dependencies  
│── 📜 README.md            # Project documentation  






