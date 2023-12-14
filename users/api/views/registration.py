from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.api.serializers.registration import RegistrationSerializer


@api_view(['POST'])
def register(request):
    serializer = RegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(data=serializer.data)
