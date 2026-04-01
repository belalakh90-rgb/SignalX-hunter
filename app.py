from flask import Flask, render_template_string, request, session, redirect
import os

app = Flask(__name__)
app.secret_key = "signalx_hunter_2026" # مفتاح الأمان

# بيانات الأدمن الخاصة بك
ADMIN_EMAIL = "netmost8@gmail.com"
ADMIN_PASS = "Hunter2026" # يمكنك تغييرها لاحقاً
USDT_TRC20 = "ضع_عنوان_محفظتك_هنا"

@app.route('/')
def home():
    return f"""
    <body style="background-color: #0b0e11; color: white; font-family: sans-serif; text-align: center; padding: 50px;">
        <h1 style="color: #f0b90b;">SignalX Hunter 🎯</h1>
        <p>نظام صيد السيولة والصفقات الآلية يعمل الآن 24/7</p>
        <hr style="border: 0.5px solid #2b2f36;">
        <div style="background: #181a20; padding: 20px; border-radius: 15px; display: inline-block; border: 1px solid #f0b90b;">
            <h3>تفعيل اشتراك VIP</h3>
            <p>ارسل 50 USDT (TRC20) إلى العنوان التالي:</p>
            <code style="background: #2b2f36; padding: 5px; color: #f0b90b;">{USDT_TRC20}</code>
            <p>بعد الدفع، راسل الأدمن: {ADMIN_EMAIL}</p>
        </div>
    </body>
    """

@app.route('/admin')
def admin_login():
    # كود صفحة تسجيل دخول الأدمن للتحكم
    return "لوحة تحكم SignalX Hunter (تحت التطوير)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
