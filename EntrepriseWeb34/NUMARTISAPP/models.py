from django.db import models

# Create your models here.


class ContactInfo(models.Model):
    address = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    

class Carousel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')


class Feature(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    color = models.CharField(max_length=7)  # For the color code

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    clients_satisfaits = models.IntegerField()
    projets_realises = models.IntegerField()
    image = models.ImageField(upload_to='about_images/')


class Icon(models.Model):
    name = models.CharField(max_length=255)
    css_class = models.CharField(max_length=255)

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='service_images/')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    category = models.CharField(max_length=100)  # For categories like 'choisissez', 'réservez', etc.

    def __str__(self):
        return self.title


class Quote(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    form_fields = models.JSONField()  # Store form fields as JSON
    image = models.ImageField(upload_to='quote_images/')

    def __str__(self):
        return self.title


class Footer(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    social_links = models.JSONField()  # Store social media links as JSON
    services = models.ManyToManyField(Service, related_name='footers')
    quick_links = models.JSONField()  # Store quick links as JSON

    def __str__(self):
        return f"Footer - {self.address}"


class NewsletterSubscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



class QuoteRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    special_note = models.TextField()

    def __str__(self):
        return f"Quote Request from {self.name}"


class FooterInfo(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.address


class PageLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title


class Company(models.Model):
    name = models.CharField(max_length=255)
    legal_structure = models.CharField(max_length=255)
    email = models.EmailField()
    business_sector = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='contacts')
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    years_of_experience = models.CharField(max_length=100)
    job_title = models.CharField(max_length=255)
    working_hours = models.CharField(max_length=100)
    id_photo = models.ImageField(upload_to='id_photos/')

    def __str__(self):
        return f"{self.full_name} - {self.company.name}"




# class ServiceForm(forms.ModelForm):
#     class Meta:
#         model = Service
#         fields = ['name', 'description', 'icon', 'link']


class UserLogin(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.email


class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Besoin', 'Besoin'),
        ('Localisation', 'Localisation'),
        ('Validation', 'Validation'),
    ]

    step = models.CharField(max_length=50, choices=STATUS_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Step: {self.step}"


class Location(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.address


class TopbarInfo(models.Model):
    address = models.CharField(max_length=255)
    hours = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"TopbarInfo({self.address}, {self.hours}, {self.phone}, {self.email})"


class ServiceRequestTracking(models.Model):
    step_choices = [
        ('1', 'Besoin'),
        ('2', 'Localisation'),
        ('3', 'Validation'),
    ]
    
    step = models.CharField(max_length=1, choices=step_choices)
    description = models.TextField()
    
    def __str__(self):
        return f"Step {self.step}: {self.description}"


class UserInformation(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    def __str__(self):
        return f"UserInformation({self.address}, {self.city}, {self.email}, {self.phone_number})"


class ServiceRequests(models.Model):
    NEED = 'besoin'
    LOCATION = 'localisation'
    VALIDATION = 'validation'
    STATUS_CHOICES = [
        (NEED, 'Besoin'),
        (LOCATION, 'Localisation'),
        (VALIDATION, 'Validation'),
    ]

    budget = models.CharField(max_length=255, help_text="Mentionner votre budget possible")
    availability = models.CharField(
        max_length=10,
        choices=[('oui', 'Oui'), ('non', 'Non')],
        default='oui'
    )
    contact_method = models.CharField(
        max_length=10,
        choices=[('telephone', 'Téléphone'), ('email', 'Email')],
        default='telephone'
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=NEED
    )

    def __str__(self):
        return f"Request {self.id} - Status: {self.get_status_display()}"


# contact

class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('mecanicien', 'Mécanicien'),
        ('electricite', 'Électricité'),
        ('plomberie', 'Plomberie'),
        ('peinture', 'Peinture'),
        ('carrelage', 'Carrelage'),
        ('maintenance', 'Maintenance'),
        ('divers', 'Divers'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"
    



class DemandeService3(models.Model):
    question1 = models.CharField(max_length=100)
    question2 = models.CharField(max_length=100)
    question3 = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    ville = models.CharField(max_length=100)
    numero = models.CharField(max_length=2000)
    budjet = models.CharField(max_length=100)
    disponibilite = models.CharField(max_length=10, choices=[('oui', 'Oui'), ('non', 'Non')], default='oui')
    contact_preference = models.CharField(max_length=10, choices=[('telephone', 'Téléphone'), ('email', 'Email')], default='email')
    def __str__(self):
        return f"{self.address}, {self.ville}, {self.email}, {self.numero}"
    

class DemandeService1(models.Model):
    DURATION_CHOICES = [
        ('30 minutes', '30 minutes'),
        ('1 heure', '1 heure'),
        ('2 heures', '2 heures'),
        ('1 jour', '1 jour'),
        ('2 jours', '2 jours'),
        ('5 jours', '5 jours'),
    ]
    ville_CHOICES = [
        ('Abidjan', 'Abidjan'),
        ('Yamoussoukro', 'Yamoussoukro'),
        ('Bouake', 'Bouake'),
        ('Daloa', 'Daloa'),
        ('San-Pedro', 'San-Pedro'),
        ('San-Rémi', 'San-Rémi'),
        ('Sassandra', 'Sassandra'),
        ('Soubre', 'Soubre'),
        ('Toumodi', 'Toumodi'),
    ]

    name = models.CharField(max_length=100, blank=False, null=True)
    demande = models.CharField(max_length=100, blank=False, null=True)
    delai = models.CharField(max_length=100, choices=DURATION_CHOICES, blank=False, null=True)
    heure = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    address = models.CharField(max_length=100, blank=False, null=True)
    ville = models.CharField(max_length=100, choices=ville_CHOICES, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    tel = models.CharField(max_length=20, blank=False, null=True)
    budget = models.DecimalField(decimal_places=2, max_digits=10, blank=False, null=True)
    indisponibilite = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return f"{self.name}, {self.demande}, {self.delai}, {self.heure}, {self.address}, {self.ville}, {self.email}, {self.tel}"

