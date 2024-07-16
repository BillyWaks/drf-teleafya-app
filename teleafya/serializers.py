from rest_framework.serializers import ModelSerializer
from teleafya.models import teleafya


class teleafyaSerializer(ModelSerializer):

    class Meta:

        model = teleafya
        fields = ('id','title','desc','is_complete')