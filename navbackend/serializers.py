from rest_framework import serializers
from .models import User,Candidate
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'