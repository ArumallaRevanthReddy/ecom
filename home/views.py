from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import Category
from home.serializers import CategorySerializer

@api_view(['GET'])
def getCategories(request):
    catgories = Category.objects.all()
    serializer = CategorySerializer(catgories, many=True)
    return Response(serializer.data)