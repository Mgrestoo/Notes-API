
from rest_framework.viewsets import ModelViewSet
from .models import Note
from .serializers import NoteSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import render


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """Register a new user"""
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response({'error': 'username and password are required'},
                        status=status.HTTP_400_BAD_REQUEST
                        )
        
    if User.objects.filter(username=username).exists():
        return Response({'error': 'username already exists'},
                        status=status.HTTP_400_BAD_REQUEST
                        )
        
    user = User.objects.create_user(username=username, password=password)
  

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    
    username = request.data.get('username')
    password = request.data.get('password')
    
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED
                        )
    if not user.check_password(password):
           return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_401_UNAUTHORIZED
                        )
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'username': user.username}, status=status.HTTP_201_CREATED)

        


class NoteViewSet(ModelViewSet):
    # queryset = Note.objects.all()
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)
    
    serializer_class = NoteSerializer
    
    permission_classes = [IsAuthenticated]
    
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    # search_fields = ['title', 'content']
    # ordering_fields = ['created_at', 'updated_at', 'title']
    
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
def login_page(request):
    return render(request, 'notes/login.html')

def register_page(request):
    return render(request, 'notes/register.html')
def notes_page(request):
    return render(request, 'notes/notes.html')

    