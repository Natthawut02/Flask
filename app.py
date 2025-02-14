from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# สร้าง Model สำหรับ Users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Route หน้าแรก
@app.route('/')
def home():
    return render_template('index.html')

# Route Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # ค้นหาผู้ใช้ในฐานข้อมูล
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="ชื่อผู้ใช้หรือรหัสผ่านผิด!")

    return render_template('login.html')

# สร้างฐานข้อมูล (ถ้ายังไม่มี)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
