from flask import Flask,render_template

app = Flask(__name__)
#라우팅 경로를 설정 /를 호출했을때 함수실행
@app.route("/")
#해당 경로에 요청이 오면 실행할 함수 정의
def hello():
    return"ddd"
@app.route("/tem")
def tem():
    #템플릿 폴더 만들어서 html저장해두면 불러와서 쓸수 있다
    return render_template('html.html')
#메인 모듈로 실행될 때 플라스크 서버 구동
if __name__ == "__main__":
    app.run()
