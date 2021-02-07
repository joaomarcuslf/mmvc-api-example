from flask_restful import Resource


class BaseResource(Resource):
    def get(self, parameter):
        pass

    def post(self, parameter):
        pass

    def put(self, parameter):
        pass

    def delete(self, parameter):
        pass


class BaseListResource(Resource):

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
