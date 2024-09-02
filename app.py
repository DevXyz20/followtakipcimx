from flask import Flask, render_template, request
from instagrapi import Client

app = Flask(__name__)

# صفحة تسجيل الدخول
@app.route('/')
def login():
    return render_template('login.html')

# التحقق من الحساب
@app.route('/verify', methods=['POST'])
def verify():
    username = request.form['username']
    password = request.form['password']

    try:
        cl = Client()
        cl.login(username, password)
        return render_template('success.html')
    except Exception as e:
        return f"Login failed: {str(e)}"

# صفحة الخيارات بعد تسجيل الدخول
@app.route('/options')
def options():
    return render_template('options.html')

# تنفيذ عملية المتابعة
@app.route('/follow', methods=['POST'])
def follow():
    target_username = request.form['target']

    cl = Client()
    cl.login('your_username', 'your_password')  # استبدل هذه القيم بحسابك الشخصي

    try:
        user_id = cl.user_id_from_username(target_username)
        cl.user_follow(user_id)
        return render_template('follow_success.html', target_username=target_username)
    except Exception as e:
        return f"Failed to follow: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
