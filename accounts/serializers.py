#     class Meta:
#         model = User
#         fields = (
#             'email', 'username', 'password', 'confirm_password', 'first_name', 'last_name'
#         )
#
#     extra_kwargs = {
#         'first_name': {'required': False},
#         'last_name': {'required': False}
#     }
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['confirm_password']:
#             raise serializers.ValidationError({
#                 'password': 'password did not match...'
#             })
#         return super(RegisterSerializers, self).validate(attrs)
#
#     def create(self, validated_data):
#         user = User.objects.create(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             first_name=validated_data['first_name', ''],
#             last_name=validated_data['last_name', ''],
#             # password=validated_data['password']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user


from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            'email', 'username', 'password', 'confirm_password', 'first_name', 'last_name'
        )

        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                'password': 'password is not match'
            })
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
