<div>
    <h1>🔍 Visual Search Engine using VLMs</h1>
    <p>A deep learning-based <strong>Visual Search Engine</strong> that retrieves similar images using <strong>Vision-Language Models (VLMs)</strong>. Supports <strong>image & text-based search</strong>, AI-powered <strong>feature extraction (ResNet-18)</strong>, and an interactive <strong>Streamlit UI</strong> for fast, efficient retrieval.</p>

    <h2>📌 Features</h2>
    <ul>
        <li>✅ <strong>Image-based search</strong> – Find visually similar images from a dataset</li>
        <li>✅ <strong>Text-based search</strong> – Retrieve images using keywords or descriptions</li>
        <li>✅ <strong>Deep Learning-powered feature extraction</strong> – Uses <strong>ResNet-18</strong></li>
        <li>✅ <strong>Fast similarity search</strong> with precomputed embeddings</li>
        <li>✅ <strong>Streamlit UI</strong> – User-friendly, interactive interface</li>
    </ul>

    <h2>🛠 Installation</h2>
    <h3>1️⃣ Clone the Repository</h3>
    <pre><code>git clone https://github.com/Krishnandu-Halder/Visual_Search_Engine_using_VLM.git
cd Visual_Search_Engine_using_VLM</code></pre>

    <h3>2️⃣ Create a Virtual Environment</h3>
    <pre><code>python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate</code></pre>

    <h3>3️⃣ Install Dependencies</h3>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h2>🚀 Usage</h2>
    <h3>1️⃣ Extract Image Features</h3>
    <pre><code>python feature_extraction.py</code></pre>

    <h3>2️⃣ Run the Web Application</h3>
    <pre><code>streamlit run app.py</code></pre>

    <h3>3️⃣ Search via Command Line</h3>
    <p>Find similar images using a query image:</p>
    <pre><code>python search.py --query path/to/query_image.jpg</code></pre>

    <p>Find images using text descriptions:</p>
    <pre><code>python search.py --text "A cat sitting on a chair"</code></pre>

    <h2>🏗 Project Structure</h2>
    <pre>
📂 Visual_Search_Engine_using_VLM
│── 📂 images/              # Dataset of images  
│── 📂 models/              # Pre-trained model storage  
│── 📜 app.py               # Streamlit UI application  
│── 📜 feature_extraction.py  # Extracts image feature vectors  
│── 📜 search.py            # CLI for searching images  
│── 📜 requirements.txt      # Required dependencies  
│── 📜 README.md            # Project documentation  
    </pre>

    <h2>🔥 Technologies Used</h2>
    <ul>
        <li>🐍 <strong>Python</strong></li>
        <li>🔥 <strong>Torch & Torchvision</strong></li>
        <li>🖼 <strong>ResNet-18</strong> (Feature Extraction)</li>
        <li>🖥 <strong>Streamlit</strong> (Web Interface)</li>
        <li>📊 <strong>NumPy & SciPy</strong> (Data Processing)</li>
    </ul>

    <h2>📌 Future Improvements</h2>
    <ul>
        <li>🔹 Support for <strong>more advanced models</strong> like CLIP & DINO</li>
        <li>🔹 <strong>Optimized search algorithms</strong> for faster retrieval</li>
        <li>🔹 <strong>Cloud deployment</strong> for scalability</li>
    </ul>

    <h2>📜 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>
</div>
