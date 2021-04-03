from flask import Flask, render_template, request
from lib.donor import Donor, insertDonor, searchDonor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def addDonor():
    return render_template('add-donor.html')


@app.route('/search', methods=['GET', 'POST'])
def searchDonors():
    if len(request.form) > 0:
        name = request.form['name']
        blood_group = request.form['blood_group'] if 'blood_group' in request.form else None
        phone = request.form['phone']
        city = request.form['city']
        result =searchDonor(
            name if name != '' else None, 
            blood_group, 
            phone if phone != '' else None, 
            city if city != '' else None
            )
        return render_template('search-donor.html', data=result)
    else:
        return render_template('search-donor.html')


@app.route('/submit_new_donor', methods=['GET', 'POST'])
def success():
    name = request.form['name']
    blood_group = request.form['blood_group']
    phone = request.form['phone']
    cnic = request.form['cnic']
    city = request.form['city']
    temp = Donor(name, blood_group, phone, cnic, city)
    if insertDonor(temp):
        return render_template('success.html')
    else:
        return render_template('failure.html')


if __name__ == '__main__':
    app.run(debug=True)
