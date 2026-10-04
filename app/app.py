import csv
import os
from pathlib import Path
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv
from src.classifier import classify_email

load_dotenv()

DATA_FILE = Path("data/processed/email_history.csv")
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

st.set_page_config(
    page_title="Support Email Classifier",
    page_icon="📩",
    layout="wide",
)

st.sidebar.title("📩 Support Email System")

page = st.sidebar.radio(
    "Navigation",
    ["Classify Email", "Admin Dashboard"],
)

if page == "Classify Email":
    st.title("📩 Support Email Classifier")
    st.write("Classify support emails by severity.")

    email = st.text_area(
        "Enter your support email",
        placeholder="Type or paste your support email here...",
        height=150,
    )

    if st.button("🚀 Classify Email"):
        if email.strip():
            category = classify_email(email)

            file_exists = DATA_FILE.exists() and DATA_FILE.stat().st_size > 0

            with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(
                    file,
                    fieldnames=["Time", "Email", "Category"],
                )

                if not file_exists:
                    writer.writeheader()

                writer.writerow({
                    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "Email": email.strip(),
                    "Category": category,
                })

            st.success(f"Email Severity: {category}")
        else:
            st.warning("Please enter an email first.")

elif page == "Admin Dashboard":
    st.title("🔐 Admin Dashboard")
    st.write("View all classified emails and categories.")

    admin_password = os.getenv("ADMIN_PASSWORD", "")
    entered_password = st.text_input(
        "Admin Password",
        type="password",
    )

    if not admin_password:
        st.error("Set ADMIN_PASSWORD in your .env file first.")

    elif st.button("Login"):
        if entered_password == admin_password:
            st.session_state["admin_logged_in"] = True
        else:
            st.session_state["admin_logged_in"] = False
            st.error("Incorrect password.")

    if st.session_state.get("admin_logged_in", False):
        if DATA_FILE.exists():
            with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
                emails = list(csv.DictReader(file))

            if emails:
                st.subheader("📊 Email Statistics")

                st.metric("Total Emails", len(emails))

                categories = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]
                cols = st.columns(4)

                for col, category in zip(cols, categories):
                    count = sum(
                        row["Category"] == category for row in emails
                    )
                    col.metric(category, count)

                st.subheader("📨 All Emails")

                selected_category = st.selectbox(
                    "Filter by Category",
                    ["ALL", "LOW", "MEDIUM", "HIGH", "CRITICAL"],
                )

                filtered_emails = emails

                if selected_category != "ALL":
                    filtered_emails = [
                        row for row in emails
                        if row["Category"] == selected_category
                    ]

                st.dataframe(
                    filtered_emails[::-1],
                    use_container_width=True,
                    hide_index=True,
                )

                st.download_button(
                    "Download Email Records (CSV)",
                    data=DATA_FILE.read_text(encoding="utf-8"),
                    file_name="email_history.csv",
                    mime="text/csv",
                )
            else:
                st.info("No classified emails available yet.")
        else:
            st.info("No emails recorded yet.")

        if st.button("Logout"):
            st.session_state["admin_logged_in"] = False
            st.rerun()
