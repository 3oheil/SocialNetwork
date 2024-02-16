from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.db.models import Q

from .serializers import UserListSerializer
from .models import Friendship

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # users = User.objects.filter(is_active=True, is_superuser=False, is_staff=False)
        q = request.query_params.get('q')
        if q:
            users = User.objects.filter(username__icontains=q)
        else:
            users = User.objects.all()
        serializers = UserListSerializer(users, many=True)
        return Response(serializers.data)


class RequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        Friendship.objects.get_or_create(request_from=request.user, request_to=user)
        return Response({'detail': 'request sent'}, status=status.HTTP_201_CREATED)


class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friend = Friendship.objects.filter(is_accepted=False, request_to=request.user)
        users = [fr.request_from for fr in friend]
        serializers = UserListSerializer(users, many=True)
        return Response(serializers.data)


class AcceptedView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')
        try:
            user = User.objects.get(pk=user_id)
            friendship: Friendship = Friendship.objects.get(is_accepted=False, request_from=user,
                                                            request_to=request.user)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        friendship.is_accepted = True
        friendship.save()

        return Response({'detail': 'Connected'})


class FriendListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friend = Friendship.objects.filter(
            Q(request_from=request.user) | Q(request_to=request.user),
            is_accepted=True
        )
        users = [fr.request_from for fr in friend]
        serializers = UserListSerializer(users, many=True)
        return Response(serializers.data)
