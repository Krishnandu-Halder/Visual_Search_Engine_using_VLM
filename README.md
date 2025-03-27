# 🔍 Visual Search Engine using VLMs

A deep learning-based **Visual Search Engine** that retrieves similar images using **Vision-Language Models (VLMs)**. It supports **image & text-based search**, AI-powered **feature extraction (ResNet-18)**, and an interactive **Streamlit UI** for efficient retrieval.

---

## 🎥 Preview
![Preview GIF](preview.gif)

---

## 📌 Features
✅ **Image-based search** – Find visually similar images from a dataset  
✅ **Text-based search** – Retrieve images using keywords or descriptions  
✅ **Deep Learning-powered feature extraction** – Uses **ResNet-18**  
✅ **Fast similarity search** with precomputed embeddings  
✅ **Streamlit UI** – User-friendly, interactive interface  

---

## 🛠 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/Krishnandu-Halder/Visual_Search_Engine_using_VLM.git
cd Visual_Search_Engine_using_VLM
```

### 2️⃣ Create a Virtual Environment
#### 🔹 **Windows**
```sh
python -m venv venv
venv\Scripts\activate
```
#### 🔹 **Linux & Mac**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

---

## 🚀 Usage
### 1️⃣ Extract Image Features
```sh
python feature_extraction.py
```

### 2️⃣ Run the Web Application
```sh
streamlit run app.py
```

### 3️⃣ Search via Command Line
#### 🔹 Find similar images using a query image:
```sh
python search.py --query path/to/query_image.jpg
```
#### 🔹 Find images using text descriptions:
```sh
python search.py --text "A cat sitting on a chair"
```

---

## 🔧 Managing Virtual Environment
### 🔹 **Activate Virtual Environment**
#### **Windows**
```sh
venv\Scripts\activate
```
#### **Linux & Mac**
```sh
source venv/bin/activate
```

### 🔹 **Deactivate Virtual Environment**
```sh
deactivate
```

---

## 🏗 Project Structure
```
📂 Visual_Search_Engine_using_VLM
│── 📂 images/              # Dataset of images  
│── 📂 models/              # Pre-trained model storage  
│── 📜 app.py               # Streamlit UI application  
│── 📜 feature_extraction.py  # Extracts image feature vectors  
│── 📜 search.py            # CLI for searching images  
│── 📜 requirements.txt      # Required dependencies  
│── 📜 README.md            # Project documentation  
```

---

## 🔥 Technologies Used
- 🐍 **Python**
- 🔥 **Torch & Torchvision**
- 🖼 **ResNet-18** (Feature Extraction)
- 🖥 **Streamlit** (Web Interface)
- 📊 **NumPy & SciPy** (Data Processing)

---

## 📌 Future Improvements
🔹 Support for **more advanced models** like CLIP & DINO  
🔹 **Optimized search algorithms** for faster retrieval  
🔹 **Cloud deployment** for scalability  

---

## 📜 License
This project is licensed under the **MIT License**.
