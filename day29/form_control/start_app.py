from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>안녕하세요~ index 화면입니다. </h1>"
    return render_template('index.html')

@app.route('/memberlist')
def memberlist():
    return render_template('memberlist.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['pwd']
        name = request.form['name']
        age = request.form['age']
        return render_template('memberlist.html', uid=uid, pwd=pwd, name=name, age=age)
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uid = request.form['uid']
        pwd = request.form['passwd']
        return render_template('index.html', uid = uid, pwd = pwd)
    else:
        return render_template('login.html')


@app.route('/output', methods=['POST'])  # post 방식
def output():
    uid = request.form['uid']  # name 값을 가져옴
    passwd = request.form['passwd']
    return render_template('output.html', uid=uid, passwd=passwd)


# 짝수/홀수 판정 프로그램
@app.route('/even_odd', methods=['GET', 'POST'])
def even_odd():
    if request.method == 'POST':
        try:
            num = int(request.form['num'])  # 입력된 숫자를 받아옴
        except ValueError:
            error_massage = "숫자를 입력해주세요"
            return render_template('/even_odd.html', error_massage=error_massage)
        else:
            if num % 2 == 0:
                result = "짝수입니다."
            else:
                result = "홀수입니다."
            return render_template('result.html', num=num, result=result)
    else:
        return render_template('even_odd.html')

    # 딕셔너리의 key=value 구조임

app.run()