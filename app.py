from flask import Flask, render_template, request, redirect, url_for
from emailprocessor import EmailProcessor  # Your email processing class

app = Flask(__name__)
email_processor = EmailProcessor()  # Initialize your email processor class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_email', methods=['POST'])
def process_email():
    if request.method == 'POST':
        email_content = request.form['email_content']
        email_summary = email_processor.summarize_email(email_content)
        suggested_action = email_processor.suggest_action(email_content)
        reply = email_processor.generate_reply(email_content)
        return render_template('index.html', summary=email_summary, action=suggested_action, reply=reply)

if __name__ == '__main__':
    app.run(debug=True)
