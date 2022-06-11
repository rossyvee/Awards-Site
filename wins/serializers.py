
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'bio', 'location', 'contact']
