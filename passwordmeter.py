import re
import streamlit as st
import random
import string

# Page setup
st.set_page_config(
    page_title="Password Strength & Generator | By Izhaar",
    page_icon="🔐",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        text-align: center;
        padding-top: 30px;
    }
    .stTextInput {
        width: 60% !important;
        margin: auto;
    }
    .stButton > button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 10px;
        border: none;
        border-radius: 8px;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #45a049;
        cursor: pointer;
    }
    .stMarkdown {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Page title
st.title("🔐 Password Strength Checker & Generator")
st.write("Secure your accounts with strong passwords. Check how strong your password is or generate a secure one instantly.")

# Password Input
password = st.text_input("🔑 Enter your password:", type="password", help="A secure password protects your digital life.")

# Strength Checker Function
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Make sure your password is at least **8 characters** long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Use a mix of **uppercase (A-Z)** and **lowercase (a-z)** letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one **number (0–9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one **special character (!@#$%^&*)**.")

    if score == 4:
        st.success("✔️ Your password is **strong and secure**.")
    elif score == 3:
        st.info("⚠️ Your password is **moderately strong**. You can make it even better.")
    else:
        st.error("❌ Your password is **weak**. Use the tips below to improve it.")

    if feedback:
        with st.expander("💡 Suggestions to Improve"):
            for tip in feedback:
                st.write(tip)

# Password Generator Function
def generate_password(length, use_upper, use_digits, use_special):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*"

    if not characters:
        return "⚠️ Please select at least one character type."

    return ''.join(random.choice(characters) for _ in range(length))

# Strength Check Button
if st.button("🔍 Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first.")

# Divider
st.markdown("---")

# Password Generator Section
st.subheader("🔧 Need a Strong Password?")
st.write("Customize and generate a strong, random password:")

col1, col2 = st.columns(2)
with col1:
    length = st.slider("Password length", 8, 32, 12)
with col2:
    use_upper = st.checkbox("Include uppercase letters (A-Z)", value=True)
    use_digits = st.checkbox("Include numbers (0-9)", value=True)
    use_special = st.checkbox("Include special characters (!@#$%^&*)", value=True)

if st.button("⚡ Generate Password"):
    generated = generate_password(length, use_upper, use_digits, use_special)
    st.code(generated, language='text')

