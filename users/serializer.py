from rest_framework import serializers

from users.models import Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=100)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            try:
                user = Users.objects.get(user=username, password=password)
            except Users.DoesNotExist:
                user = None

            if not user:
                msg = 'Usuario y/o contraseña no válido.'
                raise serializers.ValidationError(msg)

            attrs['user'] = user
            return attrs
