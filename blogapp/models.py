from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='shop/images', default='shop/images')
    Timestamp = models.DateField(auto_now_add=True)
   
    
    def __str__(self):
        return self.title + '(' + str(self.post_id) + ')'
    
class comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_post = models.ForeignKey(post, on_delete=models.CASCADE)
    
    timestamp = models.DateField(default=now)
    
    def __str__(self):
        return self.comment + '('+ str(self.comment_id)+ ')'
    
class comment_reply(models.Model):
    rply_id = models.AutoField(primary_key=True)
    rply = models.TextField()
    comment_sno = models.IntegerField(max_length=3, default=0)
    comment = models.ForeignKey(comment, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    rply_post = models.ForeignKey(post, on_delete=models.CASCADE)
    timestamp = models.DateField(default=now)
    
    def __str__(self):
        return str(self.comment) + "(" +self.rply+ ')' + str(self.rply_id)