from django.db import models


class error(models.Model):
    errordatetime = models.DateField(auto_now=False, auto_now_add=False)
    errorid = models.IntegerField(primary_key=True)
    errordescription = models.CharField(max_length=4000)
    # add more data
    class Meta:
        managed = False
        db_table = "Error_Log"
