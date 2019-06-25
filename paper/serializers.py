
from rest_framework import serializers
from .models import *



class SubjectSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"

class DomainSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"

class PagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = "__all__"

class Paper_contentsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Paper_contents
        fields = "__all__"

class ParagraphSerialiser(serializers.ModelSerializer):
    paper_id=serializers.IntegerField(source='content.paper.id')
    class Meta:
        model = Paragraph
        fields = "__all__"