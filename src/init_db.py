#!env/bin/python
from datetime import datetime

from app import db
from app.models import Record, User



# Prepare the statement to create the database
db.create_all()

#User.query.filter_by(username='alice').delete()

# Create an admin for our application
admin = User('admin', 'admintulip')
db.session.add(admin)

# Note: user_id for Alice is 2

alice = User('alice', '1234')
db.session.add(alice)

Record.query.filter_by(user_id=2).delete()

# Add a number of records into the database
expenses_alice = [{
    'description': "Salary",
    'date': "2020/09/23",
    "amount": '50000.00',
    "user_id": 2,
}, {
    'description': "Freelance income",
    'date': "2020/09/24",
    "amount": '1000.00',
    "user_id": 2,
}, {
    'description': "Investment income",
    'date': "2020/09/24",
    "amount": '500.00',
    "user_id": 2,
}, {
    'description': "Rental income",
    'date': "2020/09/24",
    "amount": '1500.00',
    "user_id": 2,
}, {
    'description': "Capital gains",
    'date': "2020/09/25",
    "amount": '2000.00',
    "user_id": 2,
}, {
    'description': "Refund",
    'date': "2020/09/25",
    "amount": '-1000.00	',
    "user_id": 2,
}, {
    'description': "Total income",
    'date': "2020/09/25",
    "amount": '54800.00',
    "user_id": 2,
},{
    'description': "Charitable donations",
    'date': "2020/09/26",
    "amount": '500.00',
    "user_id": 2,
},{
    'description': "Home office expenses",
    'date': "2020/09/26",
    "amount": '1000.00',
    "user_id": 2,
},{
    'description': "Education expenses",
    'date': "2020/09/26",
    "amount": '1500.00',
    "user_id": 2,
},{
    'description': "Total deductions",
    'date': "2020/09/26",
    "amount": '3000.00',
    "user_id": 2,
},{
    'description': "Taxable income",
    'date': "2020/09/26",
    "amount": '51800.00',
    "user_id": 2,
},{
    'description': "Tax owed",
    'date': "2020/09/26",
    "amount": '10360.00',
    "user_id": 2,
},{
    'description': "Paid",
    'date': "2020/09/26",
    "amount": '-5000.00',
    "user_id": 2,
},{
    'description': "Balance due",
    'date': "2020/09/26",
    "amount": '5360.00',
    "user_id": 2,
}]
for record_data in expenses_alice:
    record = Record(description=record_data['description'],
                    date=datetime.strptime(record_data['date'], "%Y/%m/%d").date(),
                    amount=float(record_data['amount']),
                    user_id=record_data['user_id'])
    db.session.add(record)

# Commit our changes, database is now ready.
db.session.commit()
