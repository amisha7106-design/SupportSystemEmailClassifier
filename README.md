
📩 Support Email Classifier

An AI-powered Support Email Classification System built with Python to automatically classify customer support emails based on their severity and category. The system helps support teams identify urgent emails and prioritize responses efficiently.

🎯 Project Overview

Customer support teams receive many emails every day. Manually checking every email takes time and can delay responses to critical issues.

The Support Email Classifier analyzes incoming emails, predicts their severity, and helps support teams prioritize customer requests.

✨ Features

- 📩 Classify incoming support emails.
- 🚦 Identify email severity: LOW, MEDIUM, HIGH, and CRITICAL.
- 🤖 Automatically predict severity using text-based classification rules or a trained model, depending on the implementation.
- 📊 View email classification history.
- 🗂️ Store classified emails for future reference.
- 🖥️ Interactive Streamlit user interface.
- 📈 Admin dashboard for reviewing email records and classifications.

🔄 How It Works

"Support Email Classifier Flowchart" (docs/flowchart.png)

Workflow

1. Input Email: User enters a customer support email.
2. Text Preprocessing: The system cleans and normalizes the email text.
3. Email Classification: The classifier analyzes the message.
4. Severity Prediction: The email receives a severity label — LOW, MEDIUM, HIGH, or CRITICAL.
5. Save Results: The email and its classification are stored in the history file.
6. Admin Dashboard: Support staff can review classified emails and their severity.

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- HTML, CSS, and JavaScript (if the custom frontend is enabled)
- CSV for storing email history

📁 Project Structure

support-email-classifier/
│
├── app/
│   └── app.py
│
├── src/
│   └── classifier.py
│
├── data/
│   └── processed/
│       └── email_history.csv
│
├── docs/
│   └── flowchart.png
│
├── requirements.txt
├── README.md
└── .gitignore


🧪 Example

Input email:

«Our payment system is down, and all transactions are failing. Please resolve this immediately.»

Expected output:

- Severity: HIGH or CRITICAL, depending on the classifier's configured rules.
- Purpose: Help the support team prioritize the issue.

🏢 Real-World Applications

- Customer support departments
- E-commerce businesses
- Banking and financial services
- IT helpdesk systems
- SaaS companies
- Automated ticket management systems

🚀 Future Enhancements

- Train an NLP machine learning model.
- Predict email categories such as Billing, Technical Support, and Account Issues.
- Add email notifications for critical cases.
- Integrate a database such as SQLite or PostgreSQL.
- Add response-time tracking and analytics.
- Integrate an email service API for automatic email processing.

👩‍💻 Author

Amisha Keshri

GitHub: "@amisha7106-design" (https://github.com/amisha7106-design)




