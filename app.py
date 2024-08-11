import streamlit as st

# Header using Streamlit
st.header('Welcome to Streamlit!')

# Adding custom HTML
html_content = """
<div style="background-color: #f9f9f9; padding: 20px; border-radius: 10px;">
    <h2 style="color: #4CAF50; text-align: center;">Fancy HTML Section</h2>
    <p style="font-size: 18px; text-align: justify;">
        TESTING TESTING
        <a href="https://www.streamlit.io" target="_blank" style="color: #3498db;">links</a>,
        <strong>bold text</strong>, or even images.
    </p>
    <p style="text-align: center;">
        <img src="https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" 
             alt="Streamlit Logo" width="200">
    </p>
</div>
"""

# Render the HTML content
st.markdown(html_content, unsafe_allow_html=True)
