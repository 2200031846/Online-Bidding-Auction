from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='winner',
            name='user',
            field=models.CharField(default=None, max_length=64),
        ),
    ]
