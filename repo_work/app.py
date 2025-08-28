# Flask class 가져옴
from flask import Flask, render_template
import socket  # socket 모듈 import 추가

# Flask 애플리케이션 생성(인스턴스)
app = Flask(__name__)
# route : root
# index.html 파일 렌더링 
# 컴퓨터 이름 
# 브라우저에서 http://localhost:8080/ 접속 시 아래 함수가 실행됨
@app.route('/')
def home():  # 함수명을 hello_world에서 home으로 변경
    # 컴퓨터 이름(호스트네임) 설정
    # app.debug란? : 디버그 모드에서 실행 중인지 확인 여부
    if app.debug:
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' '
    
    # index.html 템플릿을 렌더링하며 computername 변수 전달
    return render_template('index.html', computername=hostname)

# route : menu
# menu.html 파일을 렌더링함
# render_template : Render a template by name with the given context.
@app.route('/menu')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    # Flask 웹 서버 시작
    # host="0.0.0.0": 모든 네트워크 인터페이스에서 접속 허용
    # port=8080: 8080 포트에서 서버 실행
    # debug=True 옵션 추가
    app.run(host="0.0.0.0", port=8080, debug=True)
    # 실행중 출력 
    print("Flask server is running on http://localhost:8080/")
