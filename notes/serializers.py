from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
      
    def validate_title(self, value):
        """Field level validation"""
        value = value.strip()
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long")
        if not value:
            raise serializers.ValidationError("Title cannot be blank")
        return value
    
    def validate_content(self, value):
        """Field level validation"""
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Content cannot be blank")
        return value
    class Meta:
        
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']
        
        read_only_fields = ['created_at', 'updated_at', 'id']
        """A user cannot update the created_at and updated_at fields"""
      