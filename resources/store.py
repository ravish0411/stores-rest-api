from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from models.store import StoreModel

class Store(Resource):


    def get(self, name):

        store = StoreModel.get_by_name(name)

        if store:
            return store.json(), 200 #all okay
        return {"message": f"Store {name} does not exist"}, 404 #not found

    #@jwt_required()
    def post(self, name):

        if StoreModel.get_by_name(name):

            return {"message":f"Store {name} already exists"}, 400 #bad request

        store = StoreModel(name)

        store.save_to_db()

        print (store.id)
        print (store.name)
        print (store.items)

        return {"message": f"{store.json()} added successfully"}, 201 # created


    def delete(self, name):

        store = StoreModel.get_by_name(name)

        if store:
            store.delete_from_db()
            return {"message": "Store Deleted Successfully"}, 200

        return {"message": f"Store: {name} does not exist" }, 400


class Stores(Resource):
    def get(self):

        return {"Stores": [store.json() for store in StoreModel.query.all()]}

        # the above line simplifies the following code:

#############################################################################
        #items = ItemModel.query.all()

        #list = []

        #for item in items:
        #    list.append(item.json())
        #    #itemlist.append(item.json())
        #print (list)
        #return {"items": list}
#############################################################################

#In terms of lamda function, the same can also be written as:
#       return {"items": list(map(lamda x: x.json(), ItemModel.query.all()))}
