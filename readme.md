# 🏠 USA House Price Prediction

A **Streamlit** web application that predicts the estimated price of a house in the USA using a **Linear Regression** machine learning model trained on the **USA Housing** dataset.

---

## 📌 Features

* Predict house prices based on:

  * Average Area Income
  * Average Area House Age
  * Average Area Number of Rooms
  * Average Area Number of Bedrooms
  * Area Population
* Automatically calculates **Rooms per Bedroom** as an engineered feature.
* Displays the estimated house price.
* Classifies the area's population into:

  * 🟢 Low
  * 🟡 Medium
  * 🔴 High
* Simple and interactive user interface built with Streamlit.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn

---

## 📂 Project Structure

```text
USA-House-Price-Prediction/
│
├── Dataset/
│   └── USA_Housing.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The project uses the **USA Housing** dataset containing information such as:

* Average Area Income
* Average Area House Age
* Average Area Number of Rooms
* Average Area Number of Bedrooms
* Area Population
* House Price

### Feature Engineering

A new feature is created:

```python
rooms_per_bedroom = Avg. Area Number of Rooms / Avg. Area Number of Bedrooms
```

This helps improve the model by capturing the relationship between rooms and bedrooms.

---

## 🤖 Machine Learning Model

The application uses **Linear Regression** from **Scikit-learn**.

### Features Used

* Avg. Area Income
* Avg. Area House Age
* Avg. Area Number of Rooms
* Avg. Area Number of Bedrooms
* Area Population
* rooms_per_bedroom

### Target Variable

* Price

---

LIVE APP -->>>> https://house-price-prediction-awv3hvfysk3cpdqk7k5ngs.streamlit.app/

## 📈 Population Categories

Population is divided into three categories based on dataset quantiles:

| Category | Description                    |
| -------- | ------------------------------ |
| Low      | Lower 33% of population values |
| Medium   | Middle 33%                     |
| High     | Upper 34%                      |

---

## 📦 Required Libraries

Install all dependencies using:

```bash
pip install streamlit pandas scikit-learn
```

Or install from:

```bash
pip install -r requirements.txt
```

---

## 📸 Application Preview

Add screenshots of your application here.

Example:

```text
screenshots/
├── home.png
├── prediction.png
```

---

## 🔮 Future Improvements

* Save and load the trained model using Joblib.
* Add data visualisations and charts.
* Display model performance metrics (R², MAE, RMSE).
* Support multiple machine learning algorithms.
* Deploy the application using Streamlit Community Cloud.

---

## 👨‍💻 Author

**Nikhil Verma**

GitHub: https://github.com/your-username

---

## 📄 Licence

This project is licensed under the MIT Licence.

Feel free to use, modify, and share this project for educational purposes.
