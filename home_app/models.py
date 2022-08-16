from django.db import models

class Home(models.Model):
    class Meta:
        verbose_name_plural = "Home"
    fname = models.CharField(max_length=50, default='اسم')
    lname = models.CharField(max_length=50, default='فامیل')
    role = models.CharField(max_length=100)
    image = models.ImageField(default='test.png', upload_to='image')
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    github = models.CharField(max_length=200)

    def __str__(self):
        return 'Home'

class Statistics(models.Model):
    class Meta:
        verbose_name_plural = "Statistics"
    experience = models.CharField(max_length=3)
    customers = models.CharField(max_length=5)
    projects = models.CharField(max_length=5)
    awards = models.CharField(max_length=5)

    def __str__(self):
        return 'Statistics'

class AboutMe(models.Model):
    class Meta:
        verbose_name_plural = "About Me"
    title = models.CharField(max_length=70)
    body = models.TextField()
    address = models.CharField(max_length=100)
    image = models.ImageField(default='test.jpg', upload_to='image')
    city = models.CharField(max_length=70, default='ایران')
    email = models.EmailField(default='test@gmail.com')

    def __str__(self):
        return 'About Me'

class Skill(models.Model):
    tool_name = models.CharField(max_length=50)
    progress = models.CharField(max_length=3)

    def __str__(self):
        return self.tool_name

class Service(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return self.title

class Project(models.Model):
    image = models.ImageField(default='test.jpg', upload_to='image')
    project_name = models.CharField(max_length=100)
    tools = models.CharField(max_length=100)
    github_address = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name

class Comment(models.Model):
    project_name = models.CharField(max_length=60)
    description = models.TextField()
    profile_photo = models.ImageField(default='test.png', upload_to='image')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Comment from '{self.name}'"

class Message(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    body = models.TextField()

    def __str__(self):
        return f"Message from '{self.first_name}'"