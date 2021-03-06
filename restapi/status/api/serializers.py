from rest_framework import serializers
from status.models import Status 
from accounts.api.serializer import UserPublicSerializer

class StatusInlineUserSerializer(serializers.ModelSerializer):
    """
    """
    uri = serializers.SerializerMethodField(read_only=True)
    class Meta:
        """
        """
        model = Status 
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
    def get_uri(self,obj):
        """
        """
        return "api/status/{id}/".format(id=obj.id)

class StatusSerializer(serializers.ModelSerializer):
    """
    """
    uri = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only=True)
    class Meta:
        """
        """
        model = Status 
        fields = [
            'uri',
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']
    
    def get_uri(self,obj):
        """
        """
        return "api/status/{id}/".format(id=obj.id)

    # def validate_content(self, value):
    #     if len(value) > 10000:
    #         raise serializers.ValidationError("the lenght is too long")

    def validate(self, data):
        content = data.get("content",None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None :
            raise serializers.ValidationError("content or image is required")
        return data

