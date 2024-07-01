from django.shortcuts import render
from base.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from base import permissions
# Create your views here.

#Anime list and details view
class AnimeList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers
    
class AnimeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Anime.objects.all()
    serializer_class = AnimeSerializers

#Anime synonym list and details view
class AnimeSynonymList(generics.ListCreateAPIView):
    queryset = AnimeSynonym.objects.all()
    serializer_class = AnimeSynonymSerializers
    
class AnimeSynonymDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeSynonym.objects.all()
    serializer_class = AnimeSynonymSerializers

# Studio list and details view
class StudioList(generics.ListCreateAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializers
    
class StudioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializers

# Character list and details view
class CharacterList(generics.ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializers
    
class CharacterDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializers
    
# Staff list and details view
class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializers
    
class StaffDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializers
    
#Staff in anime list and details view
class StaffInAnimeList(generics.ListCreateAPIView):
    queryset = StaffInAnime.objects.all()
    serializer_class = StaffInAnimeSerializers
    
class StaffInAnimeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffInAnime.objects.all()
    serializer_class = StaffInAnimeSerializers
    
#Staff voice character list and details view
class StaffVoiceCharacterList(generics.ListCreateAPIView):
    queryset = StaffVoiceCharacter.objects.all()
    serializer_class = StaffVoiceCharacterSerializers
    
class StaffVoiceCharacterDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffVoiceCharacter.objects.all()
    serializer_class = StaffVoiceCharacterSerializers
    
#Anime produced by studio list and details view
class AnimeProducedByStudioList(generics.ListCreateAPIView):
    queryset = AnimeProducedByStudio.objects.all()
    serializer_class = AnimeProducedByStudioSerializers
    
class AnimeProducedByStudioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeProducedByStudio.objects.all()
    serializer_class = AnimeProducedByStudioSerializers

#Anime relation list and details view
class AnimeRelationList(generics.ListCreateAPIView):
    queryset = AnimeRelation.objects.all()
    serializer_class = AnimeRelationSerializers
    
class AnimeRelationDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeRelation.objects.all()
    serializer_class = AnimeRelationSerializers  
    
#Tag list and details view
class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    
class TagDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers 
    
#Anime tag list and details view
class AnimeTagList(generics.ListCreateAPIView):
    queryset = AnimeTag.objects.all()
    serializer_class = AnimeTagSerializers
    
class AnimeTagDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeTag.objects.all()
    serializer_class = AnimeTagSerializers
    
#External site list and details view
class ExternalSiteList(generics.ListCreateAPIView):
    queryset = ExternalSite.objects.all()
    serializer_class = ExternalSiteSerializers
    
class ExternalSiteDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExternalSite.objects.all()
    serializer_class = ExternalSiteSerializers 
    
#Anime external link list and details view
class AnimeExternalLinkList(generics.ListCreateAPIView):
    queryset = AnimeExternalLink.objects.all()
    serializer_class = AnimeExternalLinkSerializers
    
class AnimeExternalLinkDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = AnimeExternalLink.objects.all()
    serializer_class = AnimeExternalLinkSerializers
    
#Staff External link list and details view
class StaffExternalLinkList(generics.ListCreateAPIView):
    queryset = StaffExternalLink.objects.all()
    serializer_class = StaffExternalLinkSerializers
    
class StaffExternalLinkDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffExternalLink.objects.all()
    serializer_class = StaffExternalLinkSerializers
    
    
# Logon system:
class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    
