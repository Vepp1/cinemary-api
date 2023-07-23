
from rest_framework import serializers
from posts.models import Posts
from likes.models import Likes


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Likes.objects.filter(owner=user, post=obj).first()
            return like.id if like else None
        return None

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height < 1000:
            raise serializers.ValidationError(
                'Image height too small!'
            )
        if value.image.width > 2000:
            raise serializers.ValidationError(
                'Image width larger than 2000px!'
            )
        return value

    class Meta:
        model = Posts
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'created_at', 'updated_at',
            'title', 'content', 'image', 'genre', 'actors',
            'like_id', 'likes_count', 'comments_count',
            'director', 'release_at',
        ]
