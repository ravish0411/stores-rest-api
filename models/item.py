from db import db

class ItemModel(db.Model): #extend the classes so that the alchemy can be interacted with

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True) #we will also assign an ID to the item now
    name = db.Column(db.String(20))
    price = db.Column(db.Float(precision = 2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') #this means that the joins are no longer needed, the
                                          #sqlalchemy by looking at this knows that the items table
                                          #has a foreign key and thus the ItemModel has a relationship
                                          #with StoreModel
                                          #the same can also be done in the StoreModel

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self): #this will return a json representation of an item
        return {"name": self.name, "price": self.price, "store" : self.store_id}

    @classmethod
    def get_by_name(cls, name):
        print ("trying to retrieve item")
        return cls.query.filter_by(name=name).first()
                                                    # this will automatically create the query using the ItemModel class extended to db.Model
                                                    #No need to build any connections or cursors
                                                    #SELECT * FROM items WHERE name = name
                                                    #This will return the first row only
                                                    #And the return will be in form of ItemModel object
        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()
        #fetch_query = "SELECT * FROM items WHERE name = ?"
        #result = cursor.execute(fetch_query, (name,))
        #row = result.fetchone()
        #connection.close()

        #if row:
            #return cls(row[0], row[1]) #return an object ItemModel
            #this is a perfect scenario for argument unpacking.
            #hence:
        #    return cls(*row)
        #return None
    @classmethod
    def search_item_exist_in_store(cls, name, store):

        return cls.query.filter_by(name = name, store_id = store).first()

    def save_to_db(self): # as this is simply putting an object into the db, we no longer need
                           #separate functions for insert and update

        db.session.add(self) #no need to define the column and values because db already knows it.
        db.session.commit()
        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()
        #insert_query = "INSERT INTO items VALUES (?,?)"
        #result = cursor.execute(insert_query, (self.name, self.price))
        #connection.commit()
        #connection.close()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
