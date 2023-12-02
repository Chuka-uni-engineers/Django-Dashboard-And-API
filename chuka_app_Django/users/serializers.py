from rest_framework import serializers

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ["__all__"]
        read_only_fields = ["id", "user", "email"]


# Token serializer
# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Custom token claims
#         token["username"] = user.userAccount.account_name
#         token["account_id"] = user.userAccount.id
#         token["profile_pic"] = user.userAccount.get_profile_pic()

#         return token
