from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, unique=True)


class Animal(models.Model):
    animal_no=models.CharField(max_length=10,blank=False,primary_key=True)
    type= models.ForeignKey('Type',on_delete=models.CASCADE)
    mother=models.ForeignKey('Animal',on_delete=models.SET_NULL, related_name='mother_of',null=True)
    father=models.ForeignKey('Animal',on_delete=models.SET_NULL, related_name='father_of',null=True)
    birth_date=models.DateField()
    breed=models.CharField(max_length=50)
    def __str__(self):
        return "Animal No: "+self.animal_no+" Type: "+self.type.type_name+" Birth Date: "+str(self.birth_date)
    
class Medical(models.Model):
    animal_no=models.ForeignKey('Animal',on_delete=models.SET_NULL,null=True)
    treatment_date=models.DateField()
    treatment_name=models.CharField(max_length=50)
    treatment_cost=models.FloatField()
    treatment_description=models.CharField(max_length=100)
    def __str__(self):
        return "Animal No: "+self.animal_no.animal_no+" Treatment Date: "+str(self.treatment_date)+" Treatment Name: "+self.treatment_name+" Treatment Cost: "+str(self.treatment_cost)
    
class Staff(models.Model):
    staff_id = models.CharField(max_length=10, primary_key=True)
    staff_name = models.CharField(max_length=50)
    staff_address = models.CharField(max_length=100)
    staff_phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', message="Phone number must be 10 digits.")],
    )
    staff_email = models.EmailField()
    staff_position = models.CharField(max_length=50)
    staff_nin = models.CharField(max_length=30, unique=True)
    
    def __str__(self):
        return "Staff ID: "+self.staff_id+" Name: "+self.staff_name+" Position: "+self.staff_position
    
class Task(models.Model):
    task_id=models.CharField(max_length=10,primary_key=True)
    task_name=models.CharField(max_length=50)
    task_description=models.CharField(max_length=300)
    task_day=models.DateField()
    task_staff=models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True)
    task_animal=models.ForeignKey('Animal',on_delete=models.SET_NULL,related_name='task_animal',null=True)
    
    def __str__(self):
        return "Task ID: "+self.task_id+" Name: "+self.task_name+" Description: "+self.task_description+" Day: "+str(self.task_day)
    
    
class Event(models.Model):
    event_id=models.CharField(max_length=10,primary_key=True)
    event_name=models.CharField(max_length=50)
    event_description=models.CharField(max_length=500)
    event_date=models.DateField()
    event_time=models.TimeField()
    event_staff=models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True)
    event_animal_type=models.ForeignKey('Type',on_delete=models.SET_NULL,related_name='event_animal_type',null=True)
    
    def __str__(self):
        return "Event ID: "+self.event_id+" Name: "+self.event_name+" Description: "+self.event_description+" Date: "+str(self.event_date)+" Time: "+str(self.event_time)
    
class Task_log(models.Model):
    task_log_id=models.CharField(max_length=10,primary_key=True)
    task_log_date=models.DateField()
    task_log_time=models.TimeField()
    task_log_description=models.CharField(max_length=100)
    task_log_staff=models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True)
    task_log_task=models.ForeignKey('Task',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return "Task Log ID: "+self.task_log_id+" Date: "+str(self.task_log_date)+" Time: "+str(self.task_log_time)+" Description: "+self.task_log_description
    