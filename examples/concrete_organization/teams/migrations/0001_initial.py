# Generated by Django 4.2.5 on 2023-09-10 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("organizations", "0006_alter_organization_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "organization_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="organizations.organization",
                    ),
                ),
                ("notes", models.TextField(blank=True, default="")),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="children",
                        to="teams.department",
                    ),
                ),
            ],
            options={
                "verbose_name": "organization",
                "verbose_name_plural": "organizations",
                "ordering": ["name"],
                "abstract": False,
            },
            bases=("organizations.organization",),
        ),
    ]
