from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from smugfolioapi.models import Image_Tags

class ImageTagsView(ViewSet):
    """SmugFolio image_Tags s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single image_Tags 
        

        Returns:
            Response -- JSON serialized image_Tags 
        """
        


        try:
            image_Tags = Image_Tags.objects.get(pk=pk)
            serializer = Image_TagsSerializer(image_Tags)
            return Response(serializer.data)
        except Image_Tags.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all image_Tags

        Returns:
            Response -- JSON serialized list of image_Tags
        """
        image_Tags_ = request.query_params.get('type', None)
        image_Tags = Image_Tags.objects.all()
        if image_Tags_ is not None:
               image_Tags = image_Tags.filter(image_Tags_type_id=image_Tags_)
        serializer = Image_TagsSerializer(image_Tags, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized image_Tags instance
        """
        image_Tags = image_Tags.objects.create(
            image_tag_name = request.data["image_tag_name"]
            
        )
        serializer = Image_TagsSerializer(image_Tags)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        """Handle PUT requests for a image_Tags

        Returns:
            Response -- Empty body with 204 status code
        """

        image_Tags = Image_Tags.objects.get(pk=request.data['id'])
        image_Tags.image_tag_name = request.data["image_tag_name"]
        

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        """Handle DELETE requests for a image_Tags

        Args:
            request (object): DELETE request object
            pk (num): Accepts the argument of the primary key of a image_Tags

        Returns:
            Status: If the method completes successfully, return a HTTP response 204 
        """
        image_Tags = image_Tags.objects.get(pk=pk)
        image_Tags.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class Image_TagsSerializer(serializers.ModelSerializer):
    """JSON serializer for image_Tags s
    """
    class Meta:
        model = Image_Tags
        fields = ('id', 'image_tag_name')
        depth = 2
        

   