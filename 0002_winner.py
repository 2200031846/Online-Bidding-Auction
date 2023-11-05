from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_win_list', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auctions.auctionlist')),
            ],
        ),
    ]
