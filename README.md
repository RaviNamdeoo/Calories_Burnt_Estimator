# 🔥 Calories Burnt Estimator
 
A machine learning web app that predicts how many calories you burn during exercise — based on your body stats and workout data.
 
Built with **XGBoost** + **Streamlit**, trained on 15,000 exercise records.
 
---

✨[Click to open Deployed App](https://calories-burnt-estimation-system.streamlit.app/)

---

##  App Preview
 
Enter your details as given below:
- Gender
- Age
- Height
- Weight
- Exercise duration
- Heart rate
- Body temperature -— get an instant calorie prediction.
 
---

## 📊 Dataset
 
Two CSV files merged on `User_ID`:
 
| File | Rows | Columns |
|------|------|---------|
| `exercise.csv` | 15,000 | User_ID, Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp |
| `calories.csv` | 15,000 | User_ID, Calories |

---

## 🤖 Models Trained & Compared
 
| Model | R² Score | MSE |
|-------|----------|-----|
| Linear Regression | 0.9673 | 131.99 |
| Decision Tree Regressor | 0.9931 | 27.82 |
| Random Forest Regressor | 0.9982 | 7.22 |
| **XGBoost Regressor** | **0.9989** | **4.57** |

✅ **XGBoost** was selected as the best model.

---
 
## 🎯 Cross Validation Results (5-Fold)
 
| Model | Mean R² | Std Dev |
|-------|---------|---------|
| Linear Regression | 0.9670 | 0.0008 |
| Decision Tree | 0.9917 | 0.0005 |
| Random Forest | 0.9975 | 0.0002 |
| **XGBoost** | **0.9986** | **0.0001** |
 
Low std dev across all models confirms **no overfitting** — results are stable and reliable.
 
---
 
## ⚙️ Hyperparameter Tuning (RandomizedSearchCV)
 
Applied `RandomizedSearchCV` on XGBoost with 20 iterations and 5-fold CV.
 
**Best Parameters found:**
```
n_estimators    : 500
max_depth       : 7
learning_rate   : 0.05
subsample       : 0.8
colsample_bytree: 0.8
```
 
**Before vs After Tuning:**
 
| Metric | Before Tuning | After Tuning |
|--------|--------------|--------------|
| R² Score | 0.9989 | **0.9995** |
| MSE | 4.57 | **1.96** |
 
---

## 🛠️ How to Run Locally
 
**1. Clone the repository**
```bash
git clone https://github.com/your-username/calories-burnt-estimator.git
cd calories-burnt-estimator
```
 
**2. Install dependencies**
```bash
pip install -r requirements.txt
```
 
**3. Run the Streamlit app**
```bash
streamlit run calories_estimation_app.py
```
 
---
 
## 📦 Requirements
 
```
streamlit
pandas
numpy
xgboost
scikit-learn
pickle-mixin
```
 
---
 
## 🧠 Tech Stack
 
- **Language:** Python 3.13
- **ML Library:** scikit-learn, XGBoost
- **App Framework:** Streamlit
- **EDA:** Pandas, NumPy, Seaborn, Matplotlib
- **Model Saving:** Pickle
---
 
## 👤 Author
 
**Ravi Namdeo**
- GitHub: [@RaviNamdeoo](https://github.com/RaviNamdeoo)
- LinkedIn: [@RaviNamdeo](https://www.linkedin.com/in/ravinamdeo/)
