from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from models.store import StoreModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required = True,
    help = "This field cannot be left blank"
    )
    parser.add_argument('store_id',
    type = int,
    required = True,
    help = "Every item needs a store_id"
    )

    @jwt_required()
    def get(self, name):

        item = ItemModel.get_by_name(name)

        if item:
            return item.json(), 200 #all okay
        return {"message": f"Item {name} does not exist"}, 404 #not found

    #@jwt_required()
    def post(self, name):

        request_data = Item.parser.parse_args()#capture json data

        if StoreModel.get_by_id(request_data['store_id']):

            if ItemModel.search_item_exist_in_store(name, request_data['store_id']):

                return {"message":f"Item {name} already exists in store {request_data['store_id']}"}, 400 #bad request

            item = ItemModel(name, request_data['price'], request_data['store_id'])
            try:
                item.save_to_db()
            except:
                return {"message":"Error in inserting item"}, 500 #internal server error
            return {"message": f"{item.json()} added successfully"}, 201 # created

        return {"message": f"Store with the store id {request_data['store_id']} does not exist"}

    def put(self, name):

        request_data = Item.parser.parse_args()#capture json data

        if StoreModel.get_by_id(request_data['store_id']):

            item = ItemModel.get_by_name(name)

            if item is None:
                item = ItemModel(name, **request_data)
            else:
                item.price = request_data["price"]

            item.save_to_db()

            return item.json(), 201

        return {"message": f"Store with the store id {request_data['store_id']} does not exist"}

    def delete(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item Deleted Successfully"}, 200
        return {"message": f"Item: {name} does not exist" }, 400


class Items(Resource):
    def get(self):

        return {"items": [item.json() for item in ItemModel.query.all()]}

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
