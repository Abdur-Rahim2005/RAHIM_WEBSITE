import streamlit as st
import math

# Session state initialize
if 'expr' not in st.session_state:
    st.session_state['expr'] = ''

# হোমপেজ
st.markdown("<h1 style='text-align: center; color: blue;'>Welcome to Rahim's Website</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: gray;'>Developed by Abdul Rahim, KUET ECE '23</h2>",
            unsafe_allow_html=True)

st.write("### Features")

# Features অপশন
option = st.selectbox("Choose a feature", ("Scientific Calculator", "Grade System Calculator"))

# সাইন্টিফিক ক্যালকুলেটর
if option == "Scientific Calculator":
    st.markdown("<h3 style='color: green;'>Scientific Calculator - Casio 991 EX</h3>", unsafe_allow_html=True)

    # ক্যালকুলেটরের বাটন ডিজাইন
    col1, col2, col3, col4 = st.columns(4)

    # প্রথম সারি
    with col1:
        if st.button("7"):
            st.session_state['expr'] += "7"
        if st.button("4"):
            st.session_state['expr'] += "4"
        if st.button("1"):
            st.session_state['expr'] += "1"
        if st.button("0"):
            st.session_state['expr'] += "0"

    with col2:
        if st.button("8"):
            st.session_state['expr'] += "8"
        if st.button("5"):
            st.session_state['expr'] += "5"
        if st.button("2"):
            st.session_state['expr'] += "2"
        if st.button("."):
            st.session_state['expr'] += "."

    with col3:
        if st.button("9"):
            st.session_state['expr'] += "9"
        if st.button("6"):
            st.session_state['expr'] += "6"
        if st.button("3"):
            st.session_state['expr'] += "3"
        if st.button("Ans"):
            st.session_state['expr'] += str(st.session_state.get('ans', 0))

    with col4:
        if st.button("\u002B"):  # "+" সাইন
            st.session_state['expr'] += "+"
        if st.button("\u2212"):  # "-" সাইন
            st.session_state['expr'] += "-"
        if st.button("×"):  # গুন
            st.session_state['expr'] += "*"
        if st.button("÷"):  # ভাগ
            st.session_state['expr'] += "/"

    # বৈজ্ঞানিক অপারেশন
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        if st.button("sin"):
            st.session_state['expr'] += "math.sin("
        if st.button("cos"):
            st.session_state['expr'] += "math.cos("
        if st.button("tan"):
            st.session_state['expr'] += "math.tan("
        if st.button("log"):
            st.session_state['expr'] += "math.log("

    with col6:
        if st.button("sin⁻¹"):
            st.session_state['expr'] += "math.asin("
        if st.button("cos⁻¹"):
            st.session_state['expr'] += "math.acos("
        if st.button("tan⁻¹"):
            st.session_state['expr'] += "math.atan("
        if st.button("ln"):
            st.session_state['expr'] += "math.log1p("

    with col7:
        if st.button("x²"):
            st.session_state['expr'] += "**2"
        if st.button("√"):
            st.session_state['expr'] += "math.sqrt("
        if st.button("^"):
            st.session_state['expr'] += ""

    with col8:
        if st.button("("):
            st.session_state['expr'] += "("
        if st.button(")"):
            st.session_state['expr'] += ")"
        if st.button("Clear"):
            st.session_state['expr'] = ''

    # ফ্যাক্টরিয়াল, nPr, nCr এবং অন্যান্য বৈজ্ঞানিক ফিচার
    col9, col10, col11 = st.columns(3)

    with col9:
        if st.button("n!"):
            st.session_state['expr'] += "math.factorial("

    with col10:
        if st.button("nPr"):
            st.session_state['expr'] += "math.perm("

    with col11:
        if st.button("nCr"):
            st.session_state['expr'] += "math.comb("

    expr = st.text_input("Expression", value=st.session_state['expr'])

    if st.button("="):
        try:
            st.session_state['ans'] = eval(expr)
            st.write(f"Result: {st.session_state['ans']}")
        except:
            st.write("Invalid Expression")

# গ্রেড সিস্টেম ক্যালকুলেটর
elif option == "Grade System Calculator":
    st.markdown("<h3 style='color: green;'>Grade System Calculator</h3>", unsafe_allow_html=True)

    total_marks = st.number_input("Enter total marks", 0, 100)

    if total_marks >= 80:
        grade = 'A+'
    elif total_marks >= 70:
        grade = 'A'
    elif total_marks >= 60:
        grade = 'B'
    elif total_marks >= 50:
        grade = 'C'
    elif total_marks >= 40:
        grade = 'D'
    else:
        grade = 'F'

    if st.button("Calculate Grade"):
        st.write(f"Your grade is: {grade}")