from django.db import models

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Attack(models.Model):
	 resourse_ip = models.CharField(max_length = 16)
	 attack_type = models.CharField(max_length = 200)
	 attack_date = models.DateTimeField('date published')
	 attack_statistics = models.FileField(upload_to='uploads/')
	 attack_report = models.TextField(max_length= 500)