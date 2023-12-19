from rest_framework.views import APIView
from rest_framework.response import Response
from smakosz.models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileAPI(APIView):
    def get(self, request, user_id):
        profile = Profile.objects.get(user_id=user_id)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
