from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

def user_file_name(instance, string, filename):
    return 'user_{0}/{1}/{2}'.format(instance.user.username,  string, filename)

def data_file_name(instance, filename):
    return user_file_name(instance, 'data', filename)

def config_file_name(instance, filename):
    return user_file_name(instance, 'config', filename)

def graph_file_name(instance, filename):
    return user_file_name(instance, 'graph', filename)

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    datafile = models.FileField(upload_to=data_file_name)
    datatimestamp = models.DateTimeField()
    configfile = models.FileField(upload_to=config_file_name, null=True)
    configtimestamp = models.DateTimeField(null=True)
    graphfile = models.FileField(upload_to=graph_file_name, null=True)
    graphtimestamp = models.DateTimeField(null=True)

    @staticmethod
    def update_user_files(user, datafile, configfile):
        try:
            user = UserDetails.objects.get(user=user)
        except UserDetails.DoesNotExist:
            user = UserDetails(user=user)

        now = datetime.now()
        user.datafile = datafile
        user.datatimestamp = now
        user.configfile = configfile
        user.configtimestamp = now
        user.save()
