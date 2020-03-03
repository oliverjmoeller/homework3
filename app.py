from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():

    if request.method == 'POST':
        form = request.form
        Loan_Amount = float(form['LoanAmount'])
        NoOfPayments = float(form['NoOfPayments'])
        InterestRate = float(form['InterestRate'])

        #print(Loan_Amount)
        #print(NoOfPayments)
        #print(InterestRate)


    
        Discount_Factor = (((1+ InterestRate)**NoOfPayments)-1)/((InterestRate * (1+ InterestRate)**NoOfPayments))
        Payment_Amount = Loan_Amount/Discount_Factor


        print(Payment_Amount)



    return render_template('estimate.html', pageTitle='Loan Calculation')

if __name__ == '__main__':
    app.run(debug=True)
