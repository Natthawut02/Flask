from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from config import ADMIN_USERNAME, ADMIN_PASSWORD
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'supersecretkey'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

@app.route('/')
def home():
    with open(os.path.join(app.static_folder, 'content.txt'), 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template('index.html', content=content)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
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
@login_required
def exams():
    exams_list = ["ข้อสอบ 1", "ข้อสอบ 2", "ข้อสอบ 3"]
    return render_template('exams.html', exams=exams_list)

@app.route('/exam/<int:exam_id>')
@login_required
def exam_detail(exam_id):
    if exam_id == 1:
        exam_content = "เนื้อหาของข้อสอบ 1: ...รายละเอียด..."
    else:
        exam_content = f"เนื้อหาของข้อสอบ {exam_id}"
    return render_template('exam_detail.html', exam_content=exam_content)

@app.route('/tips')
@login_required
def tips():
    tips_list = ["ทริค 1", "ทริค 2", "ทริค 3"]
    return render_template('tips.html', tips=tips_list)

@app.route('/tip/<int:tip_id>')
@login_required
def tip_detail(tip_id):
    tip_content = f"เนื้อหาของทริค {tip_id}"
    return render_template('tip_detail.html', tip_content=tip_content)

@app.route('/questions')
@login_required
def questions():
    questions_list = ["โจทย์ 1", "โจทย์ 2", "โจทย์ 3"]
    return render_template('questions.html', questions=questions_list)

@app.route('/edit', methods=['GET', 'POST'])
@login_required
def edit():
    if current_user.username != ADMIN_USERNAME:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        action = request.form['action']
        content = request.form['content']
        
        if action == 'add':
            with open(os.path.join(app.static_folder, 'content.txt'), 'a', encoding='utf-8') as f:
                f.write(content + '\n')
            flash('Content added successfully!', 'success')
        elif action == 'edit':
            with open(os.path.join(app.static_folder, 'content.txt'), 'w', encoding='utf-8') as f:
                f.write(content)
            flash('Content updated successfully!', 'success')
        elif action == 'delete':
            os.remove(os.path.join(app.static_folder, 'content.txt'))
            flash('Content deleted successfully!', 'success')
        
        return redirect(url_for('dashboard'))
    
    return render_template('edit.html')

@app.route('/edit_user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        pass
    
    return render_template('edit_user.html', user=user)

@app.route('/admin_dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return redirect(url_for('home'))
    
    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)

@app.route('/math')
@login_required
def math():
    return render_template('math.html', subject_name="คณิตศาสตร์")

@app.route('/science')
@login_required
def science():
    return render_template('science.html', subject_name="วิทยาศาสตร์")

@app.route('/english')
@login_required
def english():
    return render_template('english.html', subject_name="ภาษาอังกฤษ")

@app.route('/physics')
@login_required
def physics():
    return render_template('physics.html', subject_name="ฟิสิกส์")

@app.route('/biology')
@login_required
def biology():
    return render_template('biology.html', subject_name="ชีววิทยา")

@app.route('/social')
@login_required
def social():
    return render_template('social.html', subject_name="สังคม")

@app.route('/thai')
@login_required
def thai():
    return render_template('thai.html', subject_name="ภาษาไทย")

@app.route('/history')
@login_required
def history():
    return render_template('history.html', subject_name="ประวัติศาสตร์")

@app.route('/chemistry')
@login_required
def chemistry():
    return render_template('chemistry.html', subject_name="เคมี")

@app.route('/get_started')
def get_started():
    return render_template('get_started.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
