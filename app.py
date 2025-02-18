from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from config import ADMIN_USERNAME, ADMIN_PASSWORD

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="ชื่อผู้ใช้หรือรหัสผ่านผิด!")

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error="ชื่อผู้ใช้นี้มีอยู่แล้ว!")
        
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/exams')
def exams():
    exams_list = ["ข้อสอบ 1", "ข้อสอบ 2", "ข้อสอบ 3"]
    return render_template('exams.html', exams=exams_list)

@app.route('/exam/<int:exam_id>')
def exam_detail(exam_id):
    if exam_id == 1:
        exam_content = "เนื้อหาของข้อสอบ 1: ...รายละเอียด..."
    else:
        exam_content = f"เนื้อหาของข้อสอบ {exam_id}"
    return render_template('exam_detail.html', exam_content=exam_content)

@app.route('/tips')
def tips():
    tips_list = ["ทริค 1", "ทริค 2", "ทริค 3"]
    return render_template('tips.html', tips=tips_list)

@app.route('/questions')
def questions():
    questions_list = ["โจทย์ 1", "โจทย์ 2", "โจทย์ 3"]
    return render_template('questions.html', questions=questions_list)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if not current_user.is_authenticated or current_user.username != ADMIN_USERNAME:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # ...existing code for handling form submission...
        pass
    
    return render_template('edit.html')

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if not current_user.is_authenticated or not current_user.is_admin:
        return redirect(url_for('home'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        # ...existing code for handling form submission...
        pass
    
    return render_template('edit_user.html', user=user)

@app.route('/admin_dashboard')
def admin_dashboard():
    if not current_user.is_authenticated or not current_user.is_admin:
        return redirect(url_for('home'))
    
    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
