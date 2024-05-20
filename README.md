# Loan Default Prediction

## Problem Statement

This project involves analyzing the credit history of customers from a financial institution. The objective is to predict possible credit defaulters upfront and help the financial institution take proactive measures to mitigate risk.

## Dataset Description

The dataset contains demographic and financial information about customers, along with their loan application status. The goal is to use this data to build a supervised learning model that can predict whether a loan applicant will default or not.

### Columns

- **Loan_ID**: Unique Loan ID
- **Gender**: Gender of the applicant
- **Married**: Marital status of the applicant
- **Dependents**: Number of dependents
- **Education**: Educational background of the applicant
- **Self_Employed**: Whether the applicant is self-employed
- **ApplicantIncome**: Income of the applicant
- **CoapplicantIncome**: Income of the co-applicant (if any)
- **LoanAmount**: Loan amount applied for
- **Loan_Amount_Term**: Term of the loan in months
- **Credit_History**: Credit history of the applicant (1 = good, 0 = bad)
- **Property_Area**: Area where the property is located (Urban, Semiurban, Rural)
- **Loan_Status**: Status of the loan application (Y = Approved, N = Rejected)

The target variable for prediction is `Loan_Status`.

## Project Overview

### Objectives

1. **Data Cleaning**: Handle missing values and preprocess the data for model training.
2. **Exploratory Data Analysis (EDA)**: Analyze and visualize the data to extract insights and identify patterns.
3. **Feature Engineering**: Create new features or modify existing ones to improve model performance.
4. **Model Building**: Train various supervised learning models to predict loan defaults.
5. **Model Evaluation**: Evaluate the models using appropriate metrics and select the best-performing one.

### Steps Involved

1. **Data Preprocessing**
   - Handle missing values.
   - Encode categorical variables.
   - Normalize or standardize numerical features.

2. **Exploratory Data Analysis (EDA)**
   - Visualize the distribution of features.
   - Analyze the relationship between features and the target variable.
   - Identify any correlations between features.

3. **Feature Engineering**
   - Create new features that might help improve model performance.
   - Perform feature selection to keep only the most relevant features.

4. **Model Training**
   - Split the data into training and testing sets.
   - Train various supervised learning models (e.g., Logistic Regression, Decision Trees, Random Forest, Gradient Boosting).
   - Tune hyperparameters using cross-validation.

5. **Model Evaluation**
   - Evaluate models using metrics such as accuracy, precision, recall, F1 score, and AUC-ROC.
   - Compare model performance and select the best model.

6. **Model Deployment**
   - Deploy the selected model using Streamlit for interactive predictions.

### Installation

To run this project, you will need the following libraries:

```sh
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

### Usage

1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/Loan_Default_Prediction.git
cd Loan_Default_Prediction
```

2. **Run the Streamlit app:**

```sh
streamlit run app.py
```

### Conclusion

By predicting potential loan defaulters, financial institutions can take proactive measures to manage risk and make informed lending decisions. This project demonstrates the use of supervised learning techniques to build an effective predictive model for loan default prediction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We thank the financial institution for providing the dataset and the open-source community for the tools and libraries used in this project.
