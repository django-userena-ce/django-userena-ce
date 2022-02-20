from django.db import migrations, models

import userena.managers


class Migration(migrations.Migration):
    dependencies = [("userena", "0001_initial")]

    operations = [
        migrations.AlterModelManagers(
            name="userenasignup",
            managers=[("objects", userena.managers.UserenaManager())],
        ),
        migrations.AlterField(
            model_name="userenasignup",
            name="email_unconfirmed",
            field=models.EmailField(
                help_text=(
                    "Temporary email address when the user requests an email change."
                ),
                max_length=254,
                verbose_name="unconfirmed email address",
                blank=True,
            ),
        ),
    ]
