from tortoise import fields,models

class Movie(models.Model):
    name = fields.CharField(max_length=50,null=False,description="电影名")
    year = fields.CharField(max_length=50,null=False,description="电影年份")




