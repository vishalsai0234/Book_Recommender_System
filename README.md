# 📚 Book Recommender System using Machine Learning

This repository contains the implementation of a **Book Recommender System** developed using **Machine Learning techniques**.  
The project suggests personalized books to users based on their preferences and interactions, using **Collaborative Filtering**, **Content-Based Filtering**, and a **Hybrid Recommender Model**.  

---

## 🧠 Project Overview
With millions of books available online, finding the right one can be overwhelming.  
This system intelligently recommends books by learning from user behavior and book metadata, making book discovery faster, easier, and more enjoyable.  

The project demonstrates how **AI** and **Data Analytics** can be applied to digital reading platforms and online libraries.

---

## 🎯 Objectives
- Develop a machine learning-based book recommender system.  
- Suggest relevant books based on user interests and ratings.  
- Combine collaborative and content-based methods for higher accuracy.  
- Build a hybrid model to overcome the cold-start problem.  
- Deploy as an interactive web application using **Flask** or **Streamlit**.

---

## 📊 Dataset Information
**Dataset:** [Book-Crossing Dataset (Kaggle)](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)  
- **Users:** 278,858 (anonymized with demographics)  
- **Books:** 271,379  
- **Ratings:** 1,149,780 (explicit + implicit)  

The dataset includes:
- User IDs and demographic data  
- Book ISBNs, titles, and metadata  
- Explicit and implicit ratings  

Data preprocessing is performed using **pandas** and **numpy**, and stored as **pickle files** for efficient access.

---
## 📁 Project Structure

Book-Recommender-System/
│
├── README.md
├── requirements.txt
├── Book_Recommender.ipynb
└── app.py


---
## 🧩 Methodology
The system consists of four main stages:

### 1️⃣ Data Preprocessing
- Handle missing values and duplicates.  
- Normalize book metadata and ratings.  
- Build a user–item rating matrix.  
- Store clean data in pickle format for faster I/O.

### 2️⃣ Model Development

**Collaborative Filtering:**
![1_Collaborative Filtering](https://github.com/user-attachments/assets/21add722-4895-43c7-b3b7-15f0e2d462d8)
*A similarity-based approach using user–item interactions.*

**Content-Based Filtering:**
![2_Content-Based Filtering](https://github.com/user-attachments/assets/02e04041-0018-4066-aec4-127c0d6e057c)
*Recommends books using metadata such as title, genre, author.*

**Hybrid Model:**
![3_Hybrid Systems](https://github.com/user-attachments/assets/db727dce-2c1c-4fa3-b771-c2ae1537b312)
*Combines both methods for more accurate and diverse suggestions.*

### 3️⃣ Evaluation
- Qualitative evaluation through sample book queries.  
- Check relevance and accuracy of recommendations.  
- User feedback to validate recommendation quality.

### 4️⃣ Deployment
- Real-time web app built using **Flask** or **Streamlit**.  
- User inputs a book title → receives a list of similar recommended books.  

---

## 🧰 Tech Stack
| Category | Tools / Libraries |
|-----------|------------------|
| Programming | Python |
| Data Handling | pandas, numpy |
| Machine Learning | scikit-learn |
| Web Framework | Flask / Streamlit |
| Visualization | matplotlib |
| Others | pickle, cosine similarity, TF-IDF |

---

## 🚀 Expected Outcomes
✅ A scalable, ML-powered recommender system.  
✅ Accurate and personalized book suggestions.  
✅ User-friendly web interface for real-time recommendations.  
✅ Demonstration of AI integration in digital libraries.  

---


## 📬 How to Run

### 🔹 Clone this repository:
```bash
git clone https://github.com/vishalsai0234/Book-Recommender-System.git
```

### 🔹 Install dependencies:
```bash
pip install -r requirements.txt
```

### 🔹 Run the recommender system:
If using *Streamlit*:
```bash
streamlit run app.py
```

### 🔹 Input Example:
```
Enter Book Title or Year of published: 1984
Recommended Books:  
1. Animal Farm by George Orwell
2. The Handmaid's Tale by Margaret Atwood
```
### 🖼 Results Screenshot
<img width="1920" height="1080" alt="Screenshot (597)" src="https://github.com/user-attachments/assets/c08f6f48-8645-430a-8f03-7d1856a3d222" />

---

## 🌟 Future Enhancements
- Integrate *NLP-based analysis* of book summaries.
- Include *user feedback loops* for continuous learning.
- Implement *Deep Learning* for contextual recommendations.
- Extend system to other domains (movies, songs, etc.).

---

## 🧾 References
1. [Roman Panarin (2023) — *Recommender System Using Machine Learning*](https://maddevs.io/blog/recommender-system-using-machine-learning/)  
2. Y. Koren, R. Bell, and C. Volinsky, “Matrix Factorization Techniques for Recommender Systems,” *IEEE Computer*, vol. 42, no. 8, pp. 30–37, 2009.  
3. [Book-Crossing Dataset on Kaggle](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

---

## 🧑‍💻 Author
**Vishal** 

---
💡 “Books find readers, and readers find books — when AI connects the two.”
---
