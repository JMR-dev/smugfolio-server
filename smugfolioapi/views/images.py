from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from smugfolioapi.models import Images, Smug_Users
from PIL import Image

class ImageView(ViewSet):
    """SmugFolio images s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single images 
        

        Returns:
            Response -- JSON serialized images 
        """
        


        try:
            images = Images.objects.get(pk=pk)
            serializer = ImagesSerializer(images)
            return Response(serializer.data)
        except Images.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all images

        Returns:
            Response -- JSON serialized list of images
        """
        images_ = request.query_params.get('type', None)
        images = Images.objects.all()
        if images_ is not None:
               images = images.filter(images_type_id=images_)
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized images instance
        """
        # object must be retrived when using a foreign key
        smug_user = Smug_Users.objects.get(pk=request.data['smug_user'])
        images = Images.objects.create(
            file_name=request.data["file_name"],
            file_path=request.data["file_path"],
            album_id=request.data["album_id"],
            smug_user=smug_user,
            upload_date = request.data["upload_date"]
        )
        serializer = ImagesSerializer(images)
        return Response(serializer.data, status=201)

    def update(self, request, pk):
        """Handle PUT requests for a images

        Returns:
            Response -- Empty body with 204 status code
        """
        # Refactor keys to match ERD
        images = Images.objects.get(pk=pk)
        images.file_name = request.data["file_name"]
        images.file_path = request.data["file_path"]
        images.album_id = request.data["album_id"]
        images.smug_user_id = request.data["skill_level"]
        images.upload_date = request.data["upload_date"]

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        """Handle DELETE requests for a images

        Args:
            request (object): DELETE request object
            pk (num): Accepts the argument of the primary key of a images

        Returns:
            Status: If the method completes successfully, return a HTTP response 204 
        """
        images = Images.objects.get(pk=pk)
        images.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class ImagesSerializer(serializers.ModelSerializer):
    """JSON serializer for images s
    """
    class Meta:
        model = Images
        fields = ('id', 'file_name', 'file_path', 'album_id', 'smug_user_id', 'upload_date')
        depth = 2
        

   