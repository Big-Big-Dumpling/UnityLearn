from flask import Flask,render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return render_template('airplane_homepage_og.html')
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
#debug=False,host='192.168.1.111',port=5000 192.168.9.106
    #ipconfig 192.168.1.111
