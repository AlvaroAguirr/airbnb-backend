from .serializer import UserDetailSerializer

from property.serializers import ReservartionListSerializer

from django.http import JsonResponse
from .models import User

from rest_framework.decorators import api_view, authentication_classes, permission_classes


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def landlord_detail(request,pk):
    user= User.objects.get(pk=pk)

    serializer = UserDetailSerializer(user,many= False)

    return JsonResponse (serializer.data, safe=False)



@api_view(['GET'])
def reservation_list(request):
    reservations = request.user.reservations.all()

    print('user del back',request.user)
    print(reservations)
    serializer= ReservartionListSerializer(reservations, many=True)
    return JsonResponse(serializer.data, safe=False)