from django.http import HttpResponse
from User.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from firstDjangoProject.serializers import UserSerializer, ImageSerializer
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from User.models import Image

# Create your views here.


@api_view(["POST"])
def CreateUser(request):
    data = request.data
    print(data)
    username = data["username"]
    password = data["password"]
    address = data["address"]
    email = data["email"]
    phone = data["phone"]

    images = request.FILES.getlist("Images", [])
    user = User(
        username=username,
        password=password,
        address=address,
        email=email,
        phone=phone,
    )
    user.save()

    list_of_images = []
    for image in images:
        image = Image(image=image)
        image.save()
        print(image)
        user.images.add(image)

    # for imageId in user.images.all():
    #     image = Image.objects.get(id=imageId)
    #     list_of_images.append(image)

    print(list_of_images)

    return Response({"message": "Record Added Successfully"}, status=200)


def Home(request):
    return HttpResponse("Home Page")


@api_view(["GET"])
def GetUsers(request):
    users = User.objects.all()
    images = Image.objects.all()

    # with rest framework we can use serializers to convert data into json format
    # user_list = []
    # for user in users:
    #     user_dict = {
    #         "username": user.username,
    #         "password": user.password,
    #         "email": user.email,
    #         "phone": user.phone,
    #         "address": user.address,
    #     }
    #     user_list.append(user_dict)

    serialized_Image_data = ImageSerializer(images, many=True)
    serialized_data = UserSerializer(users, many=True)
    # response_data = serialized_data.data + serialized_Image_data.data

    return Response(serialized_data.data, status=200)


@api_view(["PUT"])
def UpdateUser(request, id):
    user = User.objects.get(id=id)
    data = request.data

    serializer = UserSerializer(instance=user, data=data)
    if serializer.is_valid():
        serializer.save()

    return Response(
        {"message": "Record Updated Successfully", "Data": serializer.data}, status=200
    )
