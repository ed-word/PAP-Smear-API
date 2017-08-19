from django.db import models

# Create your models here.
#FI_FDiagnosis
class SVM_model(models.Model):
    
    FI_FDiagnosis = models.CharField( max_length=2,editable=False, default=0 )

    Haemoglobin = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    WBC = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    Age = models.CharField(max_length=5)

    fl_smoking_1 = '1'
    fl_smoking_3 = '3'
    SMOKING_CHOICES = ((fl_smoking_1,'1'),(fl_smoking_3,'3'),)
    Smoking = models.CharField(max_length=5,choices=SMOKING_CHOICES,default=fl_smoking_1,)

    fl_nonveg_0 = '0'
    fl_nonveg_1 = '1'
    fl_nonveg_2 = '2'
    NONVEG_CHOICES = ((fl_nonveg_0,'0'),(fl_nonveg_1,'1'),(fl_nonveg_2,'2'),)
    Nonveg = models.CharField(max_length=5,choices=NONVEG_CHOICES,default=fl_nonveg_1,)

    OccupationType_9 = '9'
    OccupationType_10 = '10'
    OccupationType_15 = '15'
    OCCUPATION_CHOICES = ((OccupationType_9,'9'),(OccupationType_10,'10'),(OccupationType_15,'15'),)
    OccupationType = models.CharField(max_length=5,choices=OCCUPATION_CHOICES,default=OccupationType_9,)

    def predict(self):
        self.save()