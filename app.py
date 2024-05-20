
import pickle
import streamlit as st

#loading the trained model
pickle_in = open('Classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()

# Defining the function which will make prediction using the data which the user input
def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):

    # Pre-processing User input
    if Gender == "Male":
        Gender = 0
    else: 
        Gender = 1

    if Married == "Yes":
        Married = 1
    else:
        Married = 0

    LoanAmount = LoanAmount / 1000

    # Convert Credit_History to numerical format
    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1

    # Making Predictions
    prediction = classifier.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

    if prediction == 0:
        pred = "Rejected"
    else:
        pred = "Approved"

    return pred

import pickle
import streamlit as st
# This is the main function in which we define our webpage
def main():
    #Front end element if a web page
    html_temp = '''
    <div style = 'background-color:yellow; padding:13px'>
    <h1 style = 'color: black; text-align: center;'>Streamlit Loan Prediction ML App </h1>
    </div>
    
    '''

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)

    #following lines create boxes in which user can enter data required to make prediction
    Gender = st.selectbox('Gender', ("Male", "Female"))
    Married = st.selectbox('Married', ("Yes", "No"))
    ApplicantIncome = st.number_input("Applicants Monthly income")
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit_History', ("Unclear Debts", "No unclear Debts"))
    result = ""

    #When 'Predict is clicked , make prediction and store it
    if st.button("Predict"):
        result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History)
        st.success("Your Loan is {}".format(result))
        print(LoanAmount)

if __name__ == '__main__':
    main()
