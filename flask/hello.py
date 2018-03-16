from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Python!'
if(__name__)=='__main__':
    app.run(debug=True)
    #开启调试模式 用户操作之后可以自动保存并渲染
