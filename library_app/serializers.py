from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
    borrower = serializers.ReadOnlyField(source="borrower.username")
    class Meta:
        model = Book
        exclude = ['branch']

