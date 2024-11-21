import uuid
from rest_framework_simplejwt.authentication import JWTAuthentication

from TourAfricaApp.models import User

class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token.get('user_id')
        if user_id:
            user_id = uuid.UUID(user_id)  # Convert the string to a UUID object
        user = User.objects.get(id=user_id)
        return user
