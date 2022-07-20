import os
from flask import Flask, render_template, request, flash, redirect, url_for
import pandas as pd
import notInFacility
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '.\\upload'
ALLOWED_EXTENSIONS = {'xls'}

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template("index.html")

#def home():
 #   return render_template("index.html")


@app.route("/data", methods=['GET', 'POST'])
def data(): 
    upload = os.listdir('.\\upload')
    if upload:
        for u in upload:
            os.remove('.\\upload\\'+ u)
    if request.method == 'POST':
        #file = request.form['file']
        #data = pd.read_excel(file)
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            
            data = notInFacility.calculate_by_day(filename)
            return render_template('data.html', data=data)
        


if __name__ == "__main__":
    app.run()