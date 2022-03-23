from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from smugfolioapi.models import Smug_Users

class SmugUserView(ViewSet):
    """SmugFolio smug_users s view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single smug_users 
        

        Returns:
            Response -- JSON serialized smug_users 
        """
        


        try:
            smug_users = Smug_Users.objects.get(pk=pk)
            serializer = Smug_UsersSerializer(smug_users)
            return Response(serializer.data)
        except Smug_Users.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all smug_users

        Returns:
            Response -- JSON serialized list of smug_users
        """
        smug_users_ = request.query_params.get('type', None)
        smug_users = Smug_Users.objects.all()
        if smug_users_ is not None:
               smug_users = smug_users.filter(smug_users_type_id=smug_users_)
        serializer = Smug_UsersSerializer(smug_users, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a smug_users

        Returns:
            Response -- Empty body with 204 status code
        """

        smug_users = smug_users.objects.get(pk=pk)
        smug_users.user = request.data["user"]
        smug_users.business_name = request.data["business_name"]
        smug_users.business_owner = request.data["business_owner"]
        

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    def destroy(self, request, pk):
        """Handle DELETE requests for a smug_users

        Args:
            request (object): DELETE request object
            pk (num): Accepts the argument of the primary key of a smug_users

        Returns:
            Status: If the method completes successfully, return a HTTP response 204 
        """
        smug_users = smug_users.objects.get(pk=pk)
        smug_users.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

class Smug_UsersSerializer(serializers.ModelSerializer):
    """JSON serializer for smug_users s
    """
    class Meta:
        model = Smug_Users
        fields = ('id', 'business_name', 'business_owner', 'user')
        depth = 2
        

   