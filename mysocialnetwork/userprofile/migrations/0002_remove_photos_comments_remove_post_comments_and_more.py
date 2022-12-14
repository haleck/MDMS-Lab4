# Generated by Django 4.1.2 on 2022-11-26 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photos",
            name="comments",
        ),
        migrations.RemoveField(
            model_name="post",
            name="comments",
        ),
        migrations.AddField(
            model_name="comments",
            name="post_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="userprofile.post",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="comments",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userprofile.user",
            ),
        ),
        migrations.AlterField(
            model_name="photos",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="userprofile.user"
            ),
        ),
        migrations.AlterField(
            model_name="points",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="userprofile.user",
            ),
        ),
    ]
