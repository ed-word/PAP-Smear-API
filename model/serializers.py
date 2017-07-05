from rest_framework import serializers

from model.models import SVM_model


class SVM_model_serializer(serializers.ModelSerializer):
    class Meta:
        model = SVM_model
        fields = ('FI_FDiagnosis', 'Haemoglobin', 'WBC', 'Age', 'Smoking', 'Nonveg', 'OccupationType')