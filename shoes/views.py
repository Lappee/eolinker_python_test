from rest_framework import status
from .models import User, Shoe
from .serializers import UserSerializer, ShoeSerializer
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListShoesView(generics.ListAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class ListUserShoesView(generics.ListAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer

    def get(self, request, *args, **kwargs):
        try:
            shoes = self.queryset.filter(user_id=request.GET.get('userid'))
            return Response(ShoeSerializer(shoes, many=True).data)
        except Shoe.DoesNotExist:
            return Response(
                data={
                    'message': 'Shoes with user id: {} does not exists'.format(kwargs['userid'])
                },
                status=status.HTTP_404_NOT_FOUND
            )


class UpdateUserShoesView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        name = request.data['name']
        phone = request.data['phone']
        shoes = request.data['shoes']
        try:
            user = self.queryset.get(name=name, phone=phone)
        except User.DoesNotExist:
            user = User.objects.create(
                name=request.data['name'],
                phone=request.data['phone']
            )
        for shoe in shoes:
            if user.shoes.get(size=shoe['size'], color=shoe['color']):
                continue
            Shoe.objects.create(
                size=shoe['size'],
                color=shoe['color'],
                user=user
            )
        user.save()
        return Response(
            data=UserSerializer(user).data,
            status=status.HTTP_200_OK
        )


