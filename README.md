<img src="![alt text](image.png)" />

## Abstract 
<p> 
 Nowadays, fetal anomalies are among the most significant challenges in maternal and child health. Unfortunately, detecting and managing fetal anomalies can be costly and may not be accessible to everyone. However, this problem can be mitigated to some extent by predicting fetal anomalies early, before they become critical, using a Fetal Anomalies Detection System Powered by Artificial Intelligence (AI), Machine Learning (ML), and Explainable AI (XAI). Early identification of potential fetal health issues is crucial as it can significantly improve the effectiveness of treatment and management options.

The system leverages two state-of-the-art ML models to predict the likelihood of fetal anomalies. By combining the strengths of these models, the system ensures higher predictive accuracy and robustness. Additionally, Explainable AI (XAI) techniques are integrated into the system, enabling it to provide interpretable results. These explainable capabilities help healthcare professionals understand the rationale behind each prediction, fostering trust and transparency in clinical decision-making.

Healthcare and biomedical fields generate vast amounts of data in the form of text, images, and other formats. However, much of this data remains underutilized and unanalyzed. The Fetal Anomalies Detection System addresses this issue by harnessing this data to predict fetal anomalies effectively.

This system can reduce costs and enhance the quality of prenatal care by identifying potential anomalies at an early stage. It is capable of handling complex medical problems and making intelligent decisions based on patient profiles, such as maternal age, gestational diabetes, fetal biometry, and amniotic fluid levels.

The system's performance is rigorously evaluated using confusion matrices, enabling the calculation of metrics such as accuracy, precision, and recall. By combining the power of AI, ML models, and explainable capabilities, this system delivers high performance, better accuracy, and interpretability, making it an indispensable tool for improving maternal and fetal health outcomes.
</p>

## Introduction
<p>
  The healthcare industry collects vast amounts of data containing valuable hidden information that can be leveraged to make effective decisions. Advanced data mining and machine learning techniques are essential for extracting meaningful insights from such data. In this study, a Fetal Anomalies Detection System (FADS) is developed using Naive Bayes and Decision Tree algorithms to predict the risk of fetal anomalies during pregnancy.
The system utilizes critical medical parameters such as maternal age, fetal biometry, amniotic fluid levels, gestational diabetes, and placental health to make predictions. The FADS predicts the likelihood of fetal anomalies, enabling early interventions and effective prenatal care. Additionally, it provides significant insights, such as identifying relationships and patterns among medical factors associated with fetal anomalies.

To enhance prediction accuracy, we employed a multilayer perceptron neural network with backpropagation as the training algorithm. The results demonstrate that the designed diagnostic system can effectively predict the risk of fetal anomalies, making it a valuable tool for improving maternal and fetal health outcomes.
</p>

### Aim
<p> 
 To predict fetal anomalies based on input parameter values provided by the user and the dataset stored in the database.
</p>

### Objective
<p>
The main objective of this study is to develop and validate a prototype utilizing an explainable AI model to improve the early detection of fetal abnormalities in obstetrics, assisting in effective decision-making and prenatal care.
</p>

### Project Scope
<p>
The project has a broad scope, as it is not intended for a specific organization. This project aims to develop a generic system that can be utilized by healthcare institutions, clinics, and research organizations. Additionally, it provides valuable support to its users, such as healthcare professionals and researchers. The system is designed to offer comprehensive summary data and insights, aiding in the early detection and management of fetal anomalies.
</p>

## System Analysis
### Modules:
- **Patient Login:-** *The patient logs into the system using their ID and password.*
- **Patient Registration:_** *If the patient is a new user, they will enter their personal details and receive a user ID and password, allowing them to log in to the system.*
- **My Details:-** *The patient can view their personal details.*
- **Anomaly Prediction:-** *The patient specifies input parameter values such as maternal age, fetal biometry, or other relevant health data. The system takes these input values and predicts fetal anomalies based on the provided data. The system will also suggest doctors or specialists based on the patient's locality.*
- **Search Doctor:-** *The patient can search for doctors or specialists by specifying their name, address, or specialization.*
- **Feedback:-** *The patient can provide feedback, which will be reported to the admin for review*
- **Doctor Login:-** *The doctor logs into the system using their user ID and password.*
- **Patient Details:-** *The doctor can view the personal and medical details of their patients.*
- **Notification:-** *The admin and doctor receive notifications about system usage, such as how many patients accessed the system and details of fetal anomalies predicted by the system.*
- **Admin Login:-** *The admin logs into the system using their ID and password.*
- **Add Doctor:-** *The admin can add new doctor details to the database.*
- **Add Dataset:-** *The admin can upload datasets related to fetal health into the database.*
- **View Doctor:-** *The admin can view details of various doctors, including their personal and professional information.*
- **View Anomalies:-** *The admin can view various fetal anomaly details stored in the database.*
- **View Patient:-** *The admin can view details of patients who accessed the system.*
- **View Feedback:-** *The admin can review feedback provided by various users of the system.*
  
### Technology Used:
- #### Languages:
  - ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  - ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
  - ![JAVASCRIPT](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
  - ![PYTHON](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
- #### FrameWork:
  - ![BOOTSTRAP](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
  - ![DJANGO](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
- #### Machine-Learning Algorithms:
 <ul>
  <li><a href="https://en.wikipedia.org/wiki/Extreme_gradient_boosting">**XGBOOST (Extreme Gradient Boosting)**</a> - Accuracy: 0.9795, AUC: 0.0000, Recall: 0.9795, Precision: 0.9798, F1: 0.9795, Kappa: 0.9692, MCC: 0.9693, TT (Sec): 0.3120</li>
  <li><a href="https://en.wikipedia.org/wiki/Extra_trees_classifier">**ET (Extra Trees Classifier)**</a> - Accuracy: 0.9789, AUC: 0.0000, Recall: 0.9789, Precision: 0.9794, F1: 0.9789, Kappa: 0.9683, MCC: 0.9686, TT (Sec): 0.2970</li>
  <li><a href="https://en.wikipedia.org/wiki/LightGBM">**LightGBM (Light Gradient Boosting Machine)**</a> - Accuracy: 0.9780, AUC: 0.0000, Recall: 0.9780, Precision: 0.9783, F1: 0.9780, Kappa: 0.9670, MCC: 0.9671, TT (Sec): 0.7390</li>
  <li><a href="https://en.wikipedia.org/wiki/Random_forest">**RF (Random Forest Classifier)**</a> - Accuracy: 0.9751, AUC: 0.0000, Recall: 0.9751, Precision: 0.9755, F1: 0.9751, Kappa: 0.9627, MCC: 0.9629, TT (Sec): 0.3610</li>
  <li><a href="https://en.wikipedia.org/wiki/Gradient_boosting">**GBC (Gradient Boosting Classifier)**</a> - Accuracy: 0.9612, AUC: 0.0000, Recall: 0.9612, Precision: 0.9617, F1: 0.9612, Kappa: 0.9418, MCC: 0.9421, TT (Sec): 1.5140</li>
  <li><a href="https://en.wikipedia.org/wiki/Decision_tree_learning">**DT (Decision Tree Classifier)**</a> - Accuracy: 0.9566, AUC: 0.0000, Recall: 0.9566, Precision: 0.9569, F1: 0.9566, Kappa: 0.9349, MCC: 0.9350, TT (Sec): 0.0300</li>
  <li><a href="https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm">**KNN (K Neighbors Classifier)**</a> - Accuracy: 0.9499, AUC: 0.0000, Recall: 0.9499, Precision: 0.9527, F1: 0.9499, Kappa: 0.9249, MCC: 0.9263, TT (Sec): 0.0470</li>
  <li><a href="https://en.wikipedia.org/wiki/AdaBoost">**ADA (Ada Boost Classifier)**</a> - Accuracy: 0.8906, AUC: 0.0000, Recall: 0.8906, Precision: 0.8950, F1: 0.8910, Kappa: 0.8359, MCC: 0.8377, TT (Sec): 0.1430</li>
  <li><a href="https://en.wikipedia.org/wiki/Logistic_regression">**LR (Logistic Regression)**</a> - Accuracy: 0.8724, AUC: 0.0000, Recall: 0.8724, Precision: 0.8772, F1: 0.8734, Kappa: 0.8086, MCC: 0.8099, TT (Sec): 0.8900</li>
  <li><a href="https://en.wikipedia.org/wiki/Ridge_regression">**Ridge (Ridge Classifier)**</a> - Accuracy: 0.8518, AUC: 0.0000, Recall: 0.8518, Precision: 0.8641, F1: 0.8537, Kappa: 0.7778, MCC: 0.7820, TT (Sec): 0.0240</li>
  <li><a href="https://en.wikipedia.org/wiki/Support_vector_machine">**SVM (SVM - Linear Kernel)**</a> - Accuracy: 0.8487, AUC: 0.0000, Recall: 0.8487, Precision: 0.8540, F1: 0.8494, Kappa: 0.7730, MCC: 0.7748, TT (Sec): 0.0410</li>
  <li><a href="https://en.wikipedia.org/wiki/Linear_discriminant_analysis">**LDA (Linear Discriminant Analysis)**</a> - Accuracy: 0.8455, AUC: 0.0000, Recall: 0.8455, Precision: 0.8601, F1: 0.8476, Kappa: 0.7682, MCC: 0.7734, TT (Sec): 0.0330</li>
  <li><a href="https://en.wikipedia.org/wiki/Quadratic_discriminant_analysis">**QDA (Quadratic Discriminant Analysis)**</a> - Accuracy: 0.7561, AUC: 0.0000, Recall: 0.7561, Precision: 0.8409, F1: 0.7597, Kappa: 0.6341, MCC: 0.6730, TT (Sec): 0.0300</li>
  <li><a href="https://en.wikipedia.org/wiki/Naive_Bayes_classifier">**NB (Naive Bayes)**</a> - Accuracy: 0.7468, AUC: 0.0000, Recall: 0.7468, Precision: 0.8214, F1: 0.7506, Kappa: 0.6202, MCC: 0.6534, TT (Sec): 0.0250</li>
  <li><a href="https://en.wikipedia.org/wiki/Dummy_classifier">**Dummy (Dummy Classifier)**</a> - Accuracy: 0.3328, AUC: 0.0000, Recall: 0.3328, Precision: 0.1107, F1: 0.1662, Kappa: 0.0000, MCC: 0.0000, TT (Sec): 0.0300</li>
</ul>

- #### ML/DL:
  - ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
  - ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
  - ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
- Database:
  - ![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
- #### Data-Set for training:
  - <a href="https://github.com/SisayNegashMengistu/fetal_anomalies_dataset/blob/main/fetal_health.csv">Click here for DATA-SET</a>
- #### IDE:
  - ![VS Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
  - ![pyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
- #### OS used for testing:
  - ![MacOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=apple&logoColor=white)
  - ![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
  - ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Run Locally

Clone the project

```bash
  git clone https://github.com/SisayNegashMengistu/XAIWithREADME
```

Go to the project directory

```bash
  cd XAIWithREADME
```

Start the server

```bash
  python manage.py runserver
```

### For a detailed Report <a href="https://github.com/Kumar-laxmi/Heart-Disease-Prediction-System/blob/main/REPORT/PYTHON%20CAPSTONE%20PROJECT%20REPORT%20(TEAM%202).pdf">Click Here</a>


## ReadMe 
click the link
<a href="https://github.com/SisayNegashMengistu/XAIWithREADME">Click Here</a>




