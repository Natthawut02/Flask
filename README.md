# work Flask

นี่คือเว็บแอปพลิเคชันที่พัฒนาด้วย Flask ซึ่งให้บริการทรัพยากรการศึกษาและฟังก์ชันต่างๆ รวมถึงการยืนยันตัวตนของผู้ใช้ การจัดการเนื้อหา และการสอบเฉพาะวิชา

## คุณสมบัติ

- การลงทะเบียนและเข้าสู่ระบบของผู้ใช้
- แดชบอร์ดผู้ดูแลระบบสำหรับการจัดการผู้ใช้
- หน้าต่างๆ ที่มีเนื้อหาการศึกษาเฉพาะวิชา
- การสอบพร้อมคำถามและคำตอบ
- เคล็ดลับและเทคนิคสำหรับวิชาต่างๆ
- การจัดการเนื้อหาสำหรับผู้ดูแลระบบ

## การติดตั้ง

1. สร้างรูปแบบการเปิดใช้งาน:
    ```bash
    python -m venv venv
    source venv/bin/activate  # บน Windows ใช้ `venv\Scripts\activate`
    ```

2. ติดตั้งที่ต้องใช้:
    ```bash
    pip install -r requirements.txt
    ```

3. ตั้งค่าฐานข้อมูล:
    ```bash
    flask db upgrade
    ```

4. รันแอปพลิเคชัน:
    ```bash
    flask run
    ```

## การใช้งาน

- เข้าถึงหน้าแรกที่ `http://127.0.0.1:5000/`
- ลงทะเบียนผู้ใช้ใหม่หรือเข้าสู่ระบบด้วยบัญชีที่มีอยู่
- นำทางผ่านหน้าต่างๆ ที่มีเนื้อหาการศึกษาและทำการสอบ
- ผู้ดูแลระบบสามารถจัดการเนื้อหาและผู้ใช้ผ่านแดชบอร์ดผู้ดูแลระบบ

## โครงสร้างโครงการ

```
flask_project/
│
├── app.py                  # ไฟล์แอปพลิเคชันหลัก
├── config.py               # ไฟล์การตั้งค่า
├── requirements.txt        # รายการของแพ็กเกจที่ต้องการ
├── templates/              
│   ├── index.html
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── exams.html
│   ├── exam_detail.html
│   ├── tips.html
│   ├── tip_detail.html
│   ├── questions.html
│   ├── edit.html
│   ├── edit_user.html
│   ├── admin_dashboard.html
│   ├── math.html
│   ├── science.html
│   ├── english.html
│   ├── physics.html
│   ├── biology.html
│   ├── social.html
│   ├── thai.html
│   ├── history.html
│   ├── chemistry.html
│   ├── get_started.html
│   └── history_exam.html
└── static/
    ├── css/
    ├── js/
    └── content.txt         # ไฟล์เนื้อหาคงที่
```

