from flask import Flask, render_template, request
import pandas as pd
import notInFacility

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])


def home():
    return render_template("index.html")


@app.route("/data", methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        #data = pd.read_excel(file)
        data = notInFacility.calculate_by_day(file)
        return render_template('data.html', data=data)
        


if __name__ == "__main__":
    app.run()