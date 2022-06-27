# создаем в корне проекта файл users.json и кладете туда пустой список
# создаем класс UsersListCreateView c двумя методами get и post
# при отработке метода GET вы должны прочитать файл и вернуть его содержимое с помощью Response
# при отработке метода POST должны получить нового юзера через body и записать его в массив файла users.json, а в респонс передать сообщение "created"
#
# данные юзера на ваше усмотрение
#
# для тех кому мало:
#
# реализуйте дополнительно:
# - вытянуть юзера по id
# - обновить полностью юзера по id
# - обновить частично юзера по id
# - удалить юзера по id


import json

from rest_framework.views import APIView
from rest_framework.response import Response

from typing import TypedDict

FILE = 'users.json'
User = TypedDict('User', {'id': int, 'name': str, 'age': int})


def read_file(file_name=FILE):
    with open(file_name) as file:
        users = json.load(file)
        return users


def write_file(data, file_name=FILE):
    with open(file_name, 'w') as file:
        json.dump(data, file)


class UsersListCreateView(APIView):
    # get all users
    def get(self, *args, **kwargs):
        try:
            users = read_file()
            return Response(users)
        except Exception as err:
            return Response({'error': str(err)})

    # post user
    def post(self, *args, **kwargs):
        try:
            users: list[User] = read_file()
            user_id = users[-1]['id'] + 1 if users else 1
            data: User = self.request.data
            data.update(id=user_id)
            users.append(data)
            write_file(users)
            return Response(data)
        except Exception as err:
            return Response({'error2': str(err)})


class UserRetrieveView(APIView):
    # get user by id
    def get(self, *args, **kwargs):
        id_user = kwargs.get('pk')
        try:
            users: list[User] = read_file()
            for user in users:
                if user['id'] == id_user:
                    return Response(user)
            return Response('not found user with this id')
        except Exception as err:
            return Response({'error3': str(err)})

    # update user by id
    def put(self, *args, **kwargs):
        id_user = kwargs.get('pk')
        new_user = self.request.data
        try:
            users: list[User] = read_file()
            for index, value in enumerate(users):
                if value['id'] == id_user:
                    index1 = index
                    users[index1] = {'id': id_user, **new_user}
                    write_file(users)
                    return Response(users[index1])

            return Response('not found user with this id')
        except Exception as err:
            return Response({'error4': str(err)})

    # update some pahrams of user by id
    def patch(self, *args, **kwargs):
        try:
            id_user = kwargs.get('pk')
            users: list[User] = read_file()
            new_user = self.request.data
            for user in users:
                if user['id'] == id_user:
                    user.update(**new_user)
                    write_file(users)
                    return Response(user)
            return Response('not found user with this id')
        except Exception as err:
            return Response({'error5': str(err)})

    # delete user by id
    def delete(self, *args, **kwargs):
        try:
            id_user = kwargs.get('pk')
            users: list[User] = read_file()
            for index, value in enumerate(users):
                if value['id'] == id_user:
                    del users[index]
                    write_file(users)
                    return Response(f'{users[index]} - deleted')
            return Response('not found user with this id')
        except Exception as err:
            return Response({'error6': str(err)})
