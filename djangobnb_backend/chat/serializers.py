from rest_framework import serializers


from .models import Conversation, ConversationMessage


from useraccount.serializer import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    users= UserDetailSerializer (many=True, read_only= True)

    class Meta:
        model=Conversation
        fields= (
            'id','users','modified_at'
        )


class ConversationDetailSerializer(serializers.ModelSerializer):
    users= UserDetailSerializer (many=True, read_only= True)

    class Meta:
        model=Conversation
        fields= ('id','users','modified_at',)


class ConversarionsMessageSerializer(serializers.ModelSerializer):
    sent_to= UserDetailSerializer(many=False, read_only= True)
    create_by= UserDetailSerializer(many=False,read_only=True)

    class Meta:
        model= ConversationMessage
        fields= ('id','body','sent_to','create_by')