from flask import Flask
import os
app=Flask(__name__)
app.debug=True




@app.route('/indianmusic',method='GET')
def indianmusic():
    return render_template(index.html)


if __name__=="__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0",port=port)
