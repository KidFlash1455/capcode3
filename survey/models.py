from django.conf import settings
from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField

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

TECHNIQUE_CHOICES = (
    ("Algorithms", "Algorithms"),
    ("Artificial Intelligence", "Artificial Intelligence"),
    ("Bayesian Methods", "Bayesian Methods"),
    ("Causal Inference", "Causal Inference"),
    ("Classification", "Classification"),
    ("Computational Tools for Data Science", "Computational Tools for Data Science"),
    ("Data Collection Design", "Data Collection Design"),
    ("Data Management", "Data Management"),
    ("Data Mining", "Data Mining"),
    ("Data Munging", "Data Munging"),
    ("Data Quality", "Data Quality"),
    ("Data Security and Privacy", "Data Security and Privacy"),
    ("Data Visualization", "Data Visualization"),
    ("Database Systems and Infrastructure", "Database Systems and Infrastructure"),
    ("Decision Science", "Decision Science"),
    ("Deep Learning", "Deep Learning"),
    ("Digital Data Curation", "Digital Data Curation"),
    ("Dynamical Models", "Dynamical Models"),
    ("Econometrics", "Econometrics"),
    ("Geographic Information Systems", "Geographic Information Systems"),
    ("Graph Theory and Graph-based Methods", "Graph Theory and Graph-based Methods"),
    ("Heterogeneous Data Integration", "Heterogeneous Data Integration"),
    ("High-Dimensional Data Analysis", "High-Dimensional Data Analysis"),
    ("Human-Computer Interaction", "Human-Computer Interaction"),
    ("Image Data Processing and Analysis", "Image Data Processing and Analysis"),
    ("Information Theory", "Information Theory"),
    ("Longitudinal Data Analysis", "Longitudinal Data Analysis"),
    ("Machine Learning", "Machine Learning"),
    ("Mathematics", "Mathematics"),
    ("Missing Data and Imputation", "Missing Data and Imputation"),
    ("Natural Language Processing", "Natural Language Processing"),
    ("Network Analysis", "Network Analysis"),
    ("Number Theory", "Number Theory"),
    ("Ontology", "Ontology"),
    ("Optimization", "Optimization"),
    ("Pattern Analysis and Classification", "Pattern Analysis and Classification"),
    ("Predictive Modeling", "Predictive Modeling"),
    ("Psychometrics", "Psychometrics"),
    ("Real-time Data Processing", "Real-time Data Processing"),
    ("Signal Processing", "Signal Processing"),
    ("Sparse Data Analysis", "Sparse Data Analysis"),
    ("Spatio-Temporal Data Analysis", "Spatio-Temporal Data Analysis"),
    ("Statistical Interference", "Statistical Interference"),
    ("Statistical Modeling", "Statistical Modeling"),
    ("Statistics", "Statistics"),
    ("Survey Methodology", "Survey Methodology"),
    ("Tensor Analysis", "Tensor Analysis"),
    ("Time Series Analysis", "Time Series Analysis"),
    ("Other", "Other"),
)
CONTACT_LIST_CHOICES = (
    ("Yes, put me on the list", "Yes, put me on the list"),
    ("No, not interested at this time", "No, not interested at this time"),
    (
        "Possibly, let's chat when the time is right",
        "Possibly, let's chat when the time is right",
    ),
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
        default="",
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
    ds_techniques = MultiSelectField(
        "Data Science Methods and Analytical Techniques (Pick the most prevalent methodology or techniques you teach or use in your data science research. Select 'Other' to list others you frequently use in the comment box. This will become a filterable list on a future version of the faculty web-site. Limit to 5-7.)",
        choices=TECHNIQUE_CHOICES,
        max_length=600,
        max_choices=7,
    )
    ds_techniques_other = models.TextField(
        "Other primary data science methods or techniques not listed above.",
        max_length=300,
        default="default",
    )
    application_domains_1 = models.CharField(
        "Application 1",
        max_length=150,
        default="default",
    )
    application_domains_2 = models.CharField(
        "Application 2",
        max_length=150,
        default="default",
    )
    application_domains_3 = models.CharField(
        "Application 3",
        max_length=150,
        default="default",
    )
    application_domains_4 = models.CharField(
        "Application 4",
        max_length=150,
        default="default",
    )
    application_domains_5 = models.CharField(
        "Application 5",
        max_length=150,
        default="default",
    )
    conclusion = models.TextField(
        "Describe how your affiliation will support the institute in the next year (e.g. volunteer for events, present research at NMDSI event, conduct workshop for NMDSI, teach data science classes, conduct and publish data science research, etc.)",
        max_length=300,
        default="default",
    )
    contact_list = models.CharField(
        "We are building a list of potential articles, blog posts, and podcasts highlighting the work of affiliated faculty. Would you like to be added to that list? (Note: No publication schedule has been determined.)",
        choices=CONTACT_LIST_CHOICES,
        max_length=150,
        default="",
    )
    thank_you = models.TextField(
        "Thank you for submitting your request to be affiliated with the Northwestern Mutual Data Science Institute. Your request will be reviewed by the program administrator within two weeks. Your email address will be added to the NMDSI affiliated faculty list and your profile added to a future version of the NMDSI web-site. Please share any questions or comments you have in the space below then click submit to close the survey",
        max_length=300,
        default="default",
        blank=True,
    )

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} "

    def get_absolute_url(self):
        return reverse("survey_detail", kwargs={"pk": self.pk})
