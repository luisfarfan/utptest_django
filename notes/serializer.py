from rest_framework import serializers

from notes.models import Notes
from users.serializer import UserSerializer


class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Notes
        fields = '__all__'
