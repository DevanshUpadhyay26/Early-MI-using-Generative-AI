
# Early Heart Attack Prediction and Generation  
**BTech Final Year Project 2024**  
**Technology Stack:** Python, Large Language Models (LLMs)

## Project Overview
This project leverages machine learning and generative models to enhance the prediction of early heart attack risks. The primary objective is to improve the accuracy and effectiveness of heart disease detection by using advanced machine learning techniques, including ensemble learning, two-stage modeling, and transformer-based architectures.

## Important Notes:
1. **Project Status**: This project is currently under patent filing and research paper submission. Therefore, the full source code is not available. Only select model files have been added to this repository.
2. **Dataset**: The dataset used in this project is proprietary and not open source. It includes data collected from healthcare institutions, research papers, and other sources.
3. **Contact Information**: For further inquiries or collaboration opportunities, feel free to reach out via the following emails:  
   - Devansh Upadhyay: devanshupadhyay26@gmail.com  
   - Shobhan Sahu: shobhan0304@gmail.com  
   - Sohail Alekar: lazertorpedo10@gmail.com  
   - Aryan Jadhav: AryanJadhav71@gmail.com  

---

## System Design

### 1. System Architecture  
The system is designed to harness the power of machine learning and generative transformers for heart disease detection. The architecture focuses on critical quality attributes like performance, scalability, and security. Below is an overview of the major components in the system:

#### Data Collection and Preprocessing  
Data was sourced from healthcare institutions (Maharashtra, India), online repositories, and research papers. This data was cleaned, preprocessed, and noise was eliminated. Feature engineering was conducted to identify factors most indicative of heart disease risk, such as age, gender, ECG changes, blood pressure, and various angiographic parameters.

#### Machine Learning Models  
We employed multiple machine learning models to predict heart attack risks. The models used include:
- Logistic Regression
- Naive Bayes
- Random Forest
- K-Nearest Neighbors
- Decision Tree
- Support Vector Machine (SVM)
- Gradient Boosting

#### Two-Stage Model  
Our two-stage approach involved:
1. **Stage 1**: Logistic Regression provided initial predictions.
2. **Stage 2**: A transformer-based model (BERT) refined the predictions using contextual data to enhance accuracy.

#### Feature Augmentation  
ECG signals were further analyzed with time-domain, frequency-domain, and non-linear features to increase model performance. Machine learning models applied to this augmented data included:
- Linear Regression
- Decision Tree Classifier
- Random Forest Classifier
- SVM Classifier
- K-Nearest Neighbor

### 2. Transformer-Based Architecture  
We implemented the **TabNet** architecture, a transformer model designed for tabular data. Additionally, we employed **LLaMA 2**, a pre-trained deep learning model for autoregressive causal language modeling, to further improve our predictions.

### 3. User Interface  
A user-friendly interface was built using the **Django** framework, providing an easy-to-use platform for healthcare professionals to interact with the model.

---

### Thank you!  
*Team*
