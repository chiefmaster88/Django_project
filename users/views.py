from rest_framework.views import APIView
from rest_framework.views import Response

class TestView(APIView):
    def get(self, *args, **kwargs):
        return Response('This is get method')
    def post(self, *args, **kwargs):
        return Response('This is post method')
    def put(self, *args, **kwargs):
        return Response('This is put method')
    def patch(self, *args, **kwargs):
        return Response('This is patch method')
    def delete(self, *args, **kwargs):
        return Response('This is del method')

some_users = [
    {'id':1, 'name':'Olya', 'age':33},
    {'id':2, 'name':'Katya', 'age':29},
    {'id':3, 'name':'Oleh', 'age':53},
    {'id':4, 'name':'Petro', 'age':73},
]

class UsersList(APIView):
    def get(self, *args, **kwargs):
        return Response(some_users)
    def post(self, *args, **kwargs):
        params = self.request.query_params.dict()
        print(params)
        new_user = self.request.data
        some_users.append(new_user)
        return Response(new_user)

class UsersFiltr(APIView):
    def get(self, *args, **kwargs):
        print(kwargs.get('id'))
        get_id = kwargs.get('id')
        for user in some_users:
            if user['id'] == get_id:
                return Response(user)
        return Response('No found')

