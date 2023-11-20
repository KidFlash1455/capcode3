from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.
STATUS_CHOICES = (
    ("Full-Time", "Full-Time"),
    ("Visiting - 2+ years at MU or UWM", "Visiting - 2+ years at MU or UWM"),
    (
        "Adjunct Faculty - 2+ years at MU or UWM",
        "Adjunct Faculty - 2+ years at MU or UWM",
    ),
    (
        "Visiting Faculty - Less than 2 years at MU or UWM",
        "Visiting Faculty - Less than 2 years at MU or UWM",
    ),
    (
        "Adjunct Faculty - Less than 2 years at MU or UWM",
        "Adjunct Faculty - Less than 2 years at MU or UWM",
    ),
    ("Faculty at other university", "Faculty at other university"),
    ("Non-faculty/Industry representative", "Non-faculty/Industry representative"),
)

UNI_CHOICES = (
    ("Marquette University", "Marquette University"),
    ("University of Wisconsin - Milwaukee", "University of Wisconsin - Milwaukee"),
    ("Other", "Other"),
)


class Survey(models.Model):
    # Contact Info
    first_name = models.CharField(max_length=100, default="Default")
    last_name = models.CharField(max_length=100, default="Default")
    suffix = models.CharField(
        "Full Name including degrees/designations to be listed on web-site and directory:",
        max_length=100,
        default="Default",
    )
    email = models.EmailField(default="Default@default.com")
    status = models.CharField(
        "What is your status at the Marquette or UW-Milwaukee?",
        max_length=100,
        choices=STATUS_CHOICES,
    )
    status_desc = models.TextField(
        "If visiting faculty, add years at this universtity/name of home university For adjunct, add years serving as an adjunct for this university and place of regular employment. For other, describe your role.",
        max_length=500,
        default="Default",
    )
    # Detailed Info
    university = models.CharField(max_length=100, choices=UNI_CHOICES, default="")
    university_desc = models.CharField(
        "If you selected other, please let us know your University or Company affiliation.",
        max_length=300,
        default="default",
    )
    school = models.CharField(
        "School and/or Department (e.g. ABC College of Business, Department of Marketing)",
        max_length=200,
        default="default",
    )
    title = models.CharField(
        "Title (as used for university related business)",
        max_length=200,
        default="default",
    )
    directory_url = models.CharField(
        "University Profile or Directory URL (this will be included in theaffiliated faculty directory in lieu of other contact information)",
        max_length=200,
        default="default",
    )
    semantic_url = models.CharField(
        "Semantic url(https://www.semanticscholar.org/faq)",
        max_length=100,
        default="default",
    )
    google_url = models.CharField(
        "Semantic url(https://scholar.google.com)",
        max_length=100,
        default="default",
    )
    research_tagline = models.CharField(
        "Research Tagline (Use 10 words or less to describe your research. This will be the tagline on in the affiliated faculty web-site and directory listing.)",
        max_length=100,
        default="default",
    )
    research_desc = models.TextField(
        "Research Description (Provide a 75-150 word general description about your research emphasizing the data science tools and methodologies you use.)",
        max_length=150,
        default="default",
    )
    research_count = models.IntegerField(
        "How many data science related research projects do you expect to work on in 2020 as PI, co-PI, or significant contributor?",
        default=0,
    )
    research_examples = models.TextField(
        "List titles of one to three recent data science related research projects that you feel highlight your work. Feel free to include citation links, if desired.",
        max_length=200,
        default="Default",
    )
    ds_class_1 = models.CharField(
        "Class 1",
        max_length=100,
        default="default",
    )
    ds_class_2 = models.CharField(
        "Class 2",
        max_length=100,
        default="default",
    )
    ds_class_3 = models.CharField(
        "Class 3",
        max_length=100,
        default="default",
    )
    # Techniques and Application

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    def get_absolute_url(self):
        return reverse("survey_detail", kwargs={"pk": self.pk})
