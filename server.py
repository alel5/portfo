from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')  #
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')  #
def html_page(page_name=None):
    return render_template(page_name)  # instead of creating a function per each


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'sth went wrong'


def write_to_file(data):
    with open('database.txt', newline="", mode='a') as txt:
        email = data['email']
        subject = data['subject']
        message = data['message']
        txt.write(f'\n{email}, {subject}, {message}')
        txt.close()


def write_to_csv(data):
    with open('database.csv', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
