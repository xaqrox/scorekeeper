from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    number = db.Column(db.String(120), unique=True)
    points_given = db.relationship('Award', backref = 'giver', lazy = 'dynamic')
    points_received = db.relationship('Award', backref = 'receiver', lazy = 'dynamic')

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '<Name %r>' % (self.name)

    def assign_id(name, number):
        '''
        Add person to db and return id.
        '''

    def add_points(amt, id):
        '''
        Add amt points to person.
        '''

    def get_points(id):
        '''
        Get total points person has.
        '''

    def get_name(id):
        '''
        Given a number, get the name.
        '''

    def get_number(id):
        '''
        Given a name, get the number
        '''

    def get_id_from_name(name):
        '''
        Given a name, return id.
        '''

    def get_id_from_num(number):
        '''
        Given a number, return id.
        '''