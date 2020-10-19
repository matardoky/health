# Generated by Django 3.1.1 on 2020-10-19 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialite', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('bgColor', models.CharField(blank=True, max_length=10, null=True)),
                ('borderColor', models.CharField(blank=True, max_length=10, null=True)),
                ('dragBgColor', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AgendaSharing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BasePatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Etablissement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Specialite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ressources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MotifConsult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('specialite', models.CharField(max_length=50)),
                ('categorie', models.CharField(max_length=50)),
                ('duree', models.TimeField()),
                ('delaiMin', models.TimeField()),
                ('delaiMax', models.TimeField()),
                ('reservable', models.BooleanField(blank=True, default=True, null=True)),
                ('color', models.CharField(blank=True, max_length=10, null=True)),
                ('bgColor', models.CharField(blank=True, max_length=10, null=True)),
                ('borderColor', models.CharField(blank=True, max_length=10, null=True)),
                ('dragBgColor', models.CharField(blank=True, max_length=10, null=True)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiScheduler.agenda')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LieuConsult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rue', models.CharField(blank=True, max_length=50, null=True)),
                ('code', models.CharField(max_length=50)),
                ('name1', models.CharField(blank=True, max_length=50, null=True)),
                ('deps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depss', to='apiScheduler.deps')),
                ('name2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='etablissements', to='apiScheduler.etablissement')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='apiScheduler.region')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ville', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villes', to='apiScheduler.ville')),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('lieu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='horaires', to='apiScheduler.lieuconsult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FichePatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=50)),
                ('phone2', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField()),
                ('adresse', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=50)),
                ('ville', models.CharField(max_length=50)),
                ('remarques', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiScheduler.basepatient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('fax', models.CharField(blank=True, max_length=50, null=True)),
                ('lieu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='apiScheduler.lieuconsult')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiScheduler.basepatient'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='lieu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiScheduler.lieuconsult'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
