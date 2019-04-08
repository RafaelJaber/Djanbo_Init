# Generated by Django 2.2 on 2019-04-06 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_telefone_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('data_exp', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_cad',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cpf',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.CPF'),
        ),
    ]
