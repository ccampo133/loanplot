# loanplot

Plot some loan data.

Requires a directory called `data` with various CSV files.

Example CSV format:

    date,type,amount,principal,interest,charges,unpaid_principal
    09/17/2016,PAYMENT,1214.74,1211.34,3.40,0.00,0.00
    ...

# Development

Set up a [virtualenv](https://virtualenv.pypa.io/en/stable/)

    virtualenv -p python3 venv

Then activate it

    source venv/bin/activate

Then install

    pip install -r requirements.txt

It's helpful to install Jupyter as well

    python3 -m pip install --upgrade pip
    python3 -m pip install jupyter

