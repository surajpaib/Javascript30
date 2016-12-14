from flask import Flask,render_template,url_for
import os
app=Flask(__name__)
app.debug=True



@app.route('/indianmusic',methods=['GET'])
def indianmusic():
    url_for('static', filename='style.css')

    return render_template('index.html')


if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="127.0.0.1",port=port)
