# Generated by Django 4.2.7 on 2023-11-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0006_alter_survey_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='ds_techniques',
            field=models.CharField(choices=[('Algorithms', 'Algorithms'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Bayesian Methods', 'Bayesian Methods'), ('Causal Inference', 'Causal Inference'), ('Classification', 'Classification'), ('Computational Tools for Data Science', 'Computational Tools for Data Science'), ('Data Collection Design', 'Data Collection Design'), ('Data Management', 'Data Management'), ('Data Mining', 'Data Mining'), ('Data Munging', 'Data Munging'), ('Data Quality', 'Data Quality'), ('Data Security and Privacy', 'Data Security and Privacy'), ('Data Visualization', 'Data Visualization'), ('Database Systems and Infrastructure', 'Database Systems and Infrastructure'), ('Decision Science', 'Decision Science'), ('Deep Learning', 'Deep Learning'), ('Digital Data Curation', 'Digital Data Curation'), ('Dynamical Models', 'Dynamical Models'), ('Econometrics', 'Econometrics'), ('Geographic Information Systems', 'Geographic Information Systems'), ('Graph Theory and Graph-based Methods', 'Graph Theory and Graph-based Methods'), ('Heterogeneous Data Integration', 'Heterogeneous Data Integration'), ('High-Dimensional Data Analysis', 'High-Dimensional Data Analysis'), ('Human-Computer Interaction', 'Human-Computer Interaction'), ('Image Data Processing and Analysis', 'Image Data Processing and Analysis'), ('Information Theory', 'Information Theory'), ('Longitudinal Data Analysis', 'Longitudinal Data Analysis'), ('Machine Learning', 'Machine Learning'), ('Mathematics', 'Mathematics'), ('Missing Data and Imputation', 'Missing Data and Imputation'), ('Natural Language Processing', 'Natural Language Processing'), ('Network Analysis', 'Network Analysis'), ('Number Theory', 'Number Theory'), ('Ontology', 'Ontology'), ('Optimization', 'Optimization'), ('Pattern Analysis and Classification', 'Pattern Analysis and Classification'), ('Predictive Modeling', 'Predictive Modeling'), ('Psychometrics', 'Psychometrics'), ('Real-time Data Processing', 'Real-time Data Processing'), ('Signal Processing', 'Signal Processing'), ('Sparse Data Analysis', 'Sparse Data Analysis'), ('Spatio-Temporal Data Analysis', 'Spatio-Temporal Data Analysis'), ('Statistical Interference', 'Statistical Interference'), ('Statistical Modeling', 'Statistical Modeling'), ('Statistics', 'Statistics'), ('Survey Methodology', 'Survey Methodology'), ('Tensor Analysis', 'Tensor Analysis'), ('Time Series Analysis', 'Time Series Analysis'), ('Other', 'Other')], default='', max_length=200, verbose_name="Data Science Methods and Analytical Techniques (Pick the most prevalent methodology or techniques you teach or use in your data science research. Select 'Other' to list others you frequently use in the comment box. This will become a filterable list on a future version of the faculty web-site. Limit to 5-7.)"),
        ),
    ]