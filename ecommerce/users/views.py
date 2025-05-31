from rest_framework.viewsets import ModelViewSet
from rest_framework.status import is_success
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models import Q
from django.utils.timezone import now, timedelta

from .models import User
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def request_otp(self, request):
        contact = request.data.get('contact')
        try:
            user = User.objects.get(Q(email=contact) | Q(phone_number=contact))
            otp = user.generate_otp()
            # TODO: integrate the SMS and email provider
            return Response({'message':'OTP sent successfully'})
        except User:
            return Response({'message': 'User not found'}, status=404)

    @action(detail=False, methods=['post'])
    def verify_otp(self, request):
        contact = request.data.get('contact')
        otp = request.data.get('otp')
        try:
            user = User.objects.get(Q(email=contact) | Q(phone_number=contact))
            if user.otp == otp and user.otp_created_at >= now() - timedelta(minutes=5):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid or expired OTP'}, status=400)
        except User:
            return Response({'error': 'User not found'}, status=404)