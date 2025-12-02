import streamlit as st

# Article content
article = """
The Internet is a global network that connects millions of private, public, academic, business, and government networks. 
It uses the standard Internet protocol suite (TCP/IP) to link devices worldwide. The Internet has greatly impacted 
communication, commerce, entertainment, and education, enabling users to share and receive information faster than ever.
"""

# Define the questions and answers
questions = [
    {
        "question": "What does TCP/IP stand for?",
        "options": [
            "A) Transfer Control Protocol/Internet Protocol",
            "B) Transport Control Protocol/Internet Protocol",
            "C) Transmission Communication Protocol/Internet Protocol",
            "D) None of the above"
        ],
        "answer": "B) Transport Control Protocol/Internet Protocol"
    },
    {
        "question": "Which industries have been impacted by the Internet?",
        "options": [
            "A) Only entertainment",
            "B) Only communication",
            "C) Communication, commerce, entertainment, and education",
            "D) Only education"
        ],
        "answer": "C) Communication, commerce, entertainment, and education"
    }
]

# Streamlit UI
st.title("Interactive Article Quiz")
st.write("Read the article below and answer the following questions:")

# Display the article
st.markdown(article)

# Function to ask the questions
def ask_question(q):
    st.subheader(q['question'])
    selected_option = st.radio("Choose an option", q['options'])
    
    if st.button("Submit"):
        if selected_option == q['answer']:
            st.success("Correct!")
        else:
            st.error(f"Wrong! The correct answer is: {q['answer']}")

# Iterate over questions
for q in questions:
    ask_question(q)
