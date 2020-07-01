from db import db

class StoreModel(db.Model): #extend the classes so that the alchemy can be interacted with

    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key = True) #we will also assign an ID to the item now
    name = db.Column(db.String(30))

    items = db.relationship('ItemModel', lazy = 'dynamic') #the sqlalchemy also knows this is a one to many
                                         #relationship; hence, this is a list of items

    def __init__(self, name):
        self.name = name

    def json(self): #this will return a json representation of an item
        return {"id": self.id, "name": self.name, "items": [item.json() for item in self.items.all()]}

    @classmethod
    def get_by_name(cls, name):

        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_by_id(cls, id):

        return cls.query.filter_by(id=id).first()


    def save_to_db(self):

        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
