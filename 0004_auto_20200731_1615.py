from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_winner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlist',
            name='active_bool',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='winner',
            name='bid_win_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlist'),
        ),
    ]
