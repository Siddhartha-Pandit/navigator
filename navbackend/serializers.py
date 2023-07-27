from rest_framework import serializers
from .models import User,Candidate,isselected
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

class SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model=isselected
        fields='__all__'