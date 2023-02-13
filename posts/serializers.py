
from rest_framework import serializers
from posts.models import Posts
from likes.models import Likes


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    like_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Likes.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Posts
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'created_at', 'updated_at',
            'title', 'content', 'image', 'genrer',
            'like_id',
        ]
