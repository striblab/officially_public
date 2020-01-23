# Generated by Django 3.0.2 on 2020-01-23 22:56

from django.db import migrations
import officials.models


class Migration(migrations.Migration):

    dependencies = [
        ('officials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subagency',
            old_name='SAbolishedDate',
            new_name='SAAbolishedDate',
        ),
        migrations.AlterField(
            model_name='agency',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='agency',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='CandRegistrationNumber',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='PositionNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='crossbyreport',
            name='SubAgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='economicstatement',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='economicstatement',
            name='PrintedDate',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='economicstatement',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='economicstatement',
            name='StatementYear',
            field=officials.models.CFBIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='horseracingbyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='horseracingbyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='horseracingbyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='AuthorityNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='ByPositionNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='CountyID',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='Designee_AuthNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='NumberSlots',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='PositionNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='SubAgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='position',
            name='temp_crossid',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='professional_activitybyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='professional_activitybyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='professional_activitybyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='AddressID',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='MasterNameID',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='StdAddressID',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='publicofficial',
            name='WatershedID_Temp',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='realpropertybyreport',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='realpropertybyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='realpropertybyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='realpropertybyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='securitiesbyreport',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='securitiesbyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='securitiesbyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='securitiesbyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='sourcesbyreport',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='sourcesbyreport',
            name='EconomicStatementID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='sourcesbyreport',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='sourcesbyreport',
            name='PubOffNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='AgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='PrimaryRecID',
            field=officials.models.CFBIntegerField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='SAStatutcite',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='SAppointee',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='SAuthority',
            field=officials.models.CFBNullBooleanField(),
        ),
        migrations.AlterField(
            model_name='subagency',
            name='SubAgencyNo',
            field=officials.models.CFBIntegerField(),
        ),
    ]
