from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    title = models.CharField(max_length=50,verbose_name= "Title")
    content=RichTextField(verbose_name="Content")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma tarihi")
    article_image=models.FileField(blank=True,null=True,verbose_name="Image")
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Article",related_name="comments")
    comment_author=models.ForeignKey("auth.User",on_delete=models.CASCADE)
    comment_title=models.CharField(max_length=50,verbose_name="Comment")
    comment_content=models.CharField(max_length=200,verbose_name="Comment")
    comment_date=models.DateTimeField(auto_now_add=True,verbose_name="Created Date")
    def __str__(self):
        return self.comment_content # admin panelinde contentle gözükmesini sağlar
    class Meta:
        ordering=['-comment_date']