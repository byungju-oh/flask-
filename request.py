from flask import Flask,render_template
from flask import request
app = Flask(__name__)

@app.route('/d')
def getform():
    # GET 방식의 경우 키밧의 쌍형태로 나타나서
    #그냥 localhost 들어갔을 때는 temp에 저장한 값이 출력되고
    # localhost:5000/?name=sss&j=ddd 형식으로 ?붙이고 키값을 집어넣으면
    #그내용이 출력 된다
    temp = request.args.get('name','user01')
    temp1 = request.args.get('j','t')

    return temp+"-"+temp1
@app.route('/')
def h():
    return render_template('po.html')

@app.route('/po',methods=['post'])


def post():
    # POST는 정보가 http body 에 들어가서 파라미터가 눈에 안보인다
    #inp에 저장된거 받음
    value = request.form['inp']
    msg = "%s 환영" %value
    return msg


if __name__=="__main__":
    app.run()
    #app.run(host='192.168.2.3', port=8080) 서버 호스트 설정가능 0000하면 어떤 호스트도가능
    #포트번호도 설정가능
