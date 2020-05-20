from django.db import models

# Create your models here.

class Device(models.Model):

    Specialization = models.CharField(max_length=200, blank=False)
    DoctorName = models.CharField(max_length=200)

    Patient = models.CharField(max_length=50)
    issues = models.CharField(max_length=50)

    class Meta:
        abstract = True
    
    def __str__(self):
        return 'Specialization: {0} issues: {1}'.format(self.Specialization, self.issues)

class Desktops(Device):
    pass

class Laptops(Device):
    pass

class Mobiles(Device):
    pass


# class Desktops(models.Model):
#     Specialization = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     Specialization = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Specialization: {0} doctorname: {1}'.format(self.Specialization, self.doctorname)
#
#
# class Laptops(models.Model):
#     Specialization = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     Specialization = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Specialization: {0} doctorname: {1}'.format(self.Specialization, self.doctorname)
#
#
# class Mobiles(models.Model):
#     Specialization = models.CharField(max_length=200, blank=False)
#     doctorname = models.IntegerField()
#
#     roomno = (
#         ('SOLD', 'Item already purchased'),
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     Specialization = models.CharField(max_length=10, roomno=roomno, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")
#
#     def __str__(self):
#         return 'Specialization: {0} doctorname: {1}'.format(self.Specialization, self.doctorname)
