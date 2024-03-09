from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        email = request.form['email']
        if not name or '@' not in email:
            return 'Error: Invalid data!'
        else:
            conn = sqlite3.connect('example.db')
            c = conn.cursor()
            c.execute("INSERT INTO Readers (name, email) VALUES (?, ?)", (name, email))
            conn.commit()
            conn.close()
            return 'Data successfully submitted!'

if __name__ == '__main__':
    app.run(debug=True)
