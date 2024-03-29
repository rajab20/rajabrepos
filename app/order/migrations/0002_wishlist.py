from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0017_alter_comment_options_comment_product_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ManyToManyField(related_name='wish_list', to='product.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wish_list', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Wish list',
                'verbose_name_plural': 'Wish list',
            },
        ),
    ]