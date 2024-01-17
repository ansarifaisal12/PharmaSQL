from dotenv import load_dotenv
load_dotenv()  # load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

# Define Your Prompt for Pharma
prompt_pharma = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name DRUGS and has the following columns - ID, NAME, 
    THERAPEUTIC_AREA, COMPOUND, PRICE \n\nFor example,
    \nExample 1 - How many drugs are there in the database?,
    the SQL command will be something like this SELECT COUNT(*) FROM DRUGS ;
    \nExample 2 - Show me all drugs for treating cardiovascular diseases,
    the SQL command will be something like this SELECT * FROM DRUGS 
    WHERE THERAPEUTIC_AREA="Cardiovascular"; 
    also, the SQL code should not have ``` in the beginning or end and SQL word in the output
    """
]

# Streamlit App for Pharma
st.set_page_config(page_title="PharmaSQL: AI-driven Insights for Pharmaceuticals", page_icon=":pill:")
st.title("AI-powered PharmaSQL: Unleashing Insights from Pharmaceutical Data")

question_pharma = st.text_input("Input: ", key="input_pharma")

submit_pharma = st.button("Ask the question")

# if submit is clicked for Pharma
if submit_pharma:
    response_pharma = get_gemini_response(question_pharma, prompt_pharma)
    print(response_pharma)
    response_pharma = read_sql_query(response_pharma, "pharma.db")
    st.subheader("The Response is")
    for row_pharma in response_pharma:
        print(row_pharma)
        st.header(row_pharma)
