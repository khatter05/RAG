# 🌞 Solar Technology AI Agent

## 📌 Overview

This AI-powered assistant specializes in **solar industry consulting**, providing expert guidance through a **Streamlit-based** user interface. The assistant:

👉 **Processes user queries** and retrieves relevant information from a **ChromaDB vector database**\
👉 Uses **Ollama embeddings (mxbai-embed-large)** for context understanding\
👉 Generates detailed responses using **DeepSeek-R1**\
👉 Demonstrates expertise in **AI integration, embeddings, and real-time inference**

---

## ⚙️ Project Setup

### **Prerequisites**

Ensure you have the following installed:\
🔹 Python **3.10+**\
🔹 Ollama installed \
🔹 Required Python dependencies

### **Installation Steps**

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/khatter05/RAG.git
cd RAG
```

2️⃣ **Create & Activate a Virtual Environment**

```bash
python -m venv venv
# On macOS/Linux
source venv/bin/activate  
# On Windows
venv\Scripts\activate
```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Streamlit App**

```bash
streamlit run app.py
```

---

## 🛠️ How It Works

### **1️⃣ Data Preparation**

📂 **Context File:** The knowledge base is stored in `data/context/text.md`.\
🔍 **Embeddings Generation:** `mxbai-embed-large` generates embeddings.\
🗃️ **Storage:** These embeddings are saved in a **ChromaDB vector database**.

### **2️⃣ Query Processing**

💬 **User submits a query** via the Streamlit UI.\
📌 The query is **converted into an embedding** and matched against stored vectors in ChromaDB.\
🔍 The **most relevant context** is retrieved.

### **3️⃣ Response Generation**

🧠 The **retrieved context is fed into DeepSeek-R1**.\
📢 The AI **generates a detailed response**.\
✅ The response is **displayed on the Streamlit UI** for the user.

---

## 📊 Logging & Debugging

📁 Logs are stored in the `logs/` folder.\
📝 Example responses and images are also **logged for analysis**.

---

## 🔥 Example Use Cases



🖼️ **Screenshots** of the UI:




![Screenshot 2025-02-23 000609](https://github.com/user-attachments/assets/d8457c64-3e68-44af-9cc0-38949780ae99)



![Screenshot 2025-02-23 000615](https://github.com/user-attachments/assets/b5b207ad-96f2-4f44-b7ac-0ef5d3ef2222)



---

## 🚀 Future Improvements

✔️ **Cloud Deployment:** Host the application on **AWS/GCP/Azure**.\
✔️ **Enhanced Knowledge Base:** Expand the **vector database** with more **detailed** and **structured** information.\
✔️ **Advanced AI Models:** Leverage **heavier Ollama models** for **higher accuracy** and **better reasoning**.

---

💡 **This project was developed as part of an internship assignment for Wattmonk Technologies.**

