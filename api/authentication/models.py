from django.db import models

# Create your models here.
class CategoryService (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)

class Services (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}'


class Experience (models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_current_work_in_company = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    id = models.AutoField

    


class Education (models.Model):
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    from_year = models.IntegerField(4)
    to_year = models.IntegerField(4)
    description = models.CharField(max_length=500)
    id = models.AutoField
class Skills(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField

    def __str__(self):
        return f'{self.name}'

class RegisterFreelancer(models.Model):
    id = models.AutoField
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=11)
    password=models.CharField(max_length=300)
    job_title=models.CharField(null=True,max_length=300)
    overview=models.CharField(max_length=500,null=True)
    user_image=models.ImageField(upload_to='images/freelancer/profile/',null=True,)
    street_address=models.CharField(max_length=50,null=True,)
    city=models.CharField(max_length=50,null=True,)
    state=models.CharField(max_length=50,null=True,)
    postal_code=models.CharField(max_length=20,null=True,)
    experience=models.ManyToManyField(Experience,null=True,)
    education=models.ManyToManyField(Education,null=True,)
    skills=models.ManyToManyField(Skills,null=True,)
    services=models.ManyToManyField(Services,null=True,)
    is_complete_date=models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return  f'{self.first_name} {self.last_name}'

class RegisterUser(models.Model):
    id = models.AutoField
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    phone=models.CharField(max_length=11)
    email=models.EmailField(max_length=70)
    password=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    image=models.ImageField(upload_to='images/user_profile/')
    street=models.CharField(max_length=50, null=True, )
    city=models.CharField(max_length=50, null=True, )
    state=models.CharField(max_length=50, null=True, )
    postal_code=models.CharField(max_length=20, null=True, )
    is_online = models.BooleanField(default=False)
    def __str__(self):
        return  f'{self.fname} {self.lname}'
