import streamlit as st
from checker import check_articles

st.title("Article Checker (a / an / the)")
st.write("Upload a text file or type directly to check article usage.")

option = st.radio("Choose input type:", ["Upload File", "Type Text"])

text = ""

if option == "Upload File":
    uploaded = st.file_uploader("Upload a .txt file", type=["txt"])
    if uploaded:
        text = uploaded.read().decode("utf-8")
        st.text_area("File Content", text, height=200)

else:
    text = st.text_area("Enter your text here:")

if st.button("Check Articles"):
    if not text.strip():
        st.warning("Please provide text.")
    else:
        issues = check_articles(text)
        if issues:
            st.error("Issues Found:")
            for issue in issues:
                st.write("- ", issue)
        else:
            st.success("No article issues found!")
