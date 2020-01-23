# Generated by Django 3.0.2 on 2020-01-23 22:33

from django.db import migrations, models
import officials.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('AgencyNo', models.IntegerField()),
                ('AName', models.CharField(blank=True, max_length=255)),
                ('AAddress', models.CharField(blank=True, max_length=100)),
                ('AStreet', models.CharField(blank=True, max_length=50)),
                ('ACity', models.CharField(blank=True, max_length=50)),
                ('AState', models.CharField(blank=True, max_length=15)),
                ('AZip', models.CharField(blank=True, max_length=25)),
                ('AContact', models.CharField(blank=True, max_length=100)),
                ('ATelephone', models.CharField(blank=True, max_length=30)),
                ('AEmail', models.CharField(blank=True, max_length=75)),
                ('AWebsite', models.CharField(blank=True, max_length=100)),
                ('SenateConf', models.BooleanField()),
                ('NeedsConf', models.CharField(blank=True, max_length=50)),
                ('Statutcite', models.CharField(blank=True, max_length=50)),
                ('Reporting_Cite', models.CharField(blank=True, max_length=50)),
                ('Establishment_Cite', models.CharField(blank=True, max_length=50)),
                ('CertifiedDate', officials.models.CFBDateField(null=True)),
                ('Abolished', models.BooleanField()),
                ('AbolishedDate', officials.models.CFBDateField(null=True)),
                ('Authority', models.CharField(blank=True, max_length=100)),
                ('Appointee', models.CharField(blank=True, max_length=50)),
                ('ADisplayName', models.CharField(blank=True, max_length=100)),
                ('HasSubAgency', models.BooleanField()),
                ('AHas_Attachment', models.BooleanField()),
                ('AAttachment', models.CharField(blank=True, max_length=255)),
                ('Memo', models.CharField(blank=True, max_length=255)),
                ('ASend_InterOffice_Mail', models.BooleanField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('msrepl_tran_version', models.CharField(blank=True, max_length=40)),
                ('bySeat', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='CrossbyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('EconomicStatementID', models.IntegerField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
                ('AgencyNo', models.IntegerField()),
                ('SubAgencyNo', models.IntegerField()),
                ('PositionNo', models.IntegerField()),
                ('POTitle', models.CharField(blank=True, max_length=500)),
                ('DateReceived', officials.models.CFBDateTimeField(null=True)),
                ('Terminated', models.BooleanField()),
                ('TerminationDate', officials.models.CFBDateTimeField(null=True)),
                ('ReAppoint', models.BooleanField()),
                ('ReportIn', models.BooleanField()),
                ('ReportInDate', officials.models.CFBDateField(null=True)),
                ('ApptDate', officials.models.CFBDateField(null=True)),
                ('TermEndDate', officials.models.CFBDateField(null=True)),
                ('PermStatus', models.BooleanField()),
                ('Replaced', models.BooleanField()),
                ('POLastReportFiled', officials.models.CFBDateField(null=True)),
                ('IsCandidate', models.BooleanField()),
                ('CandType', models.CharField(blank=True, max_length=25)),
                ('CandRegistrationNumber', models.IntegerField(null=True)),
                ('CandidateDelete', models.BooleanField()),
                ('MoreThanOneBoard', models.BooleanField()),
                ('TemporaryPublicOfficial', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EconomicStatement',
            fields=[
                ('EconomicStatementID', models.IntegerField(primary_key=True, serialize=False)),
                ('PubOffNo', models.IntegerField()),
                ('OnlineApplicationIDs', models.CharField(blank=True, max_length=255)),
                ('ScenarioType', models.CharField(max_length=30)),
                ('StatementYear', models.IntegerField(db_index=True)),
                ('DueDate', officials.models.CFBDateField()),
                ('OriginalCertDate', officials.models.CFBDateTimeField(null=True)),
                ('AmendedDate', officials.models.CFBDateTimeField(null=True)),
                ('ProcessedDate', officials.models.CFBDateTimeField(null=True)),
                ('PrintedDate', models.NullBooleanField()),
                ('ElectronicFiler', models.BooleanField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HorseRacingbyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('EconomicStatementID', models.IntegerField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
                ('InterestDesc', models.TextField()),
                ('PartialInterest', models.BooleanField()),
                ('FullInterest', models.BooleanField()),
                ('Interest', models.TextField()),
                ('AgencyNo', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PositionNo', models.IntegerField()),
                ('AgencyNo', models.IntegerField()),
                ('SubAgencyNo', models.IntegerField()),
                ('Title', models.CharField(blank=True, max_length=150)),
                ('AuthorityNo', models.IntegerField(null=True)),
                ('ByPosition', models.BooleanField()),
                ('ByPositionNo', models.IntegerField(null=True)),
                ('ByPositionDesc', models.CharField(blank=True, max_length=50)),
                ('MayDesignate', models.BooleanField()),
                ('IsTempTitle', models.BooleanField()),
                ('Designee_AuthNo', models.IntegerField(null=True)),
                ('temp_crossid', models.IntegerField(null=True)),
                ('SenateConf', models.BooleanField()),
                ('NeedsConf', models.CharField(blank=True, max_length=50)),
                ('Statutcite', models.CharField(blank=True, max_length=50)),
                ('Reporting_Cite', models.CharField(blank=True, max_length=50)),
                ('Establishment_Cite', models.CharField(blank=True, max_length=50)),
                ('CountyID', models.IntegerField(null=True)),
                ('CandidateDistrict', models.CharField(blank=True, max_length=5)),
                ('NumberSlots', models.IntegerField(null=True)),
                ('UnlimitedSlots', models.BooleanField()),
                ('bySeat', models.BooleanField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('msrepl_tran_version', models.CharField(blank=True, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Professional_ActivitybyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('EconomicStatementID', models.IntegerField()),
                ('Professional_Activity', models.CharField(blank=True, max_length=150)),
                ('Employee', models.BooleanField()),
                ('Contractor', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicOfficial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('SirName', models.CharField(blank=True, max_length=10)),
                ('POFirstName', models.CharField(blank=True, max_length=50)),
                ('POMI', models.CharField(blank=True, max_length=5)),
                ('POLastName', models.CharField(blank=True, max_length=50)),
                ('POSuffix', models.CharField(blank=True, max_length=7)),
                ('POAddress', models.CharField(blank=True, max_length=100)),
                ('POStreet', models.CharField(blank=True, max_length=50)),
                ('POCity', models.CharField(blank=True, max_length=50)),
                ('POState', models.CharField(blank=True, max_length=15)),
                ('POZip', models.CharField(blank=True, max_length=25)),
                ('POTelephone', models.CharField(blank=True, max_length=30)),
                ('POEmail', models.CharField(blank=True, max_length=75)),
                ('POOccupation', models.CharField(blank=True, max_length=150)),
                ('POEmployer', models.CharField(blank=True, max_length=150)),
                ('POBusAddr', models.CharField(blank=True, max_length=150)),
                ('POBusStreet', models.CharField(blank=True, max_length=50)),
                ('POBusCity', models.CharField(blank=True, max_length=50)),
                ('POBusState', models.CharField(blank=True, max_length=15)),
                ('POBusZip', models.CharField(blank=True, max_length=25)),
                ('OldNo', models.CharField(blank=True, max_length=10)),
                ('POBusSameAsHome', models.BooleanField()),
                ('EIS_AnnualSent', models.BooleanField()),
                ('EIS_AnnualSentDate', officials.models.CFBDateTimeField(null=True)),
                ('PreLastUpdate', officials.models.CFBDateTimeField(null=True)),
                ('POLastUpdate', officials.models.CFBDateTimeField(null=True)),
                ('RecentRecertDate', officials.models.CFBDateTimeField(null=True)),
                ('CandidateDelete', models.BooleanField()),
                ('Send_InterOffice_Mail', models.BooleanField()),
                ('hideProperty', models.BooleanField()),
                ('WatershedID_Temp', models.IntegerField(null=True)),
                ('POHas_Attachment', models.BooleanField()),
                ('POAttachment', models.CharField(blank=True, max_length=255)),
                ('POMemo', models.CharField(blank=True, max_length=255)),
                ('Waiver2ndHome', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('msrepl_tran_version', models.CharField(blank=True, max_length=40)),
                ('MasterNameID', models.IntegerField(null=True)),
                ('StdAddressID', models.NullBooleanField()),
                ('AddressID', models.NullBooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RealPropertyByReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('EconomicStatementID', models.IntegerField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
                ('Address', models.CharField(blank=True, max_length=255)),
                ('Municipality', models.CharField(blank=True, max_length=50)),
                ('County', models.CharField(blank=True, max_length=75)),
                ('Acreage', models.CharField(blank=True, max_length=75)),
                ('Fee', models.BooleanField()),
                ('Mortgage', models.BooleanField()),
                ('Contract', models.BooleanField()),
                ('Option2500', models.BooleanField()),
                ('Option50000', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('AgencyNo', models.IntegerField(null=True)),
                ('CandidateDelete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SecuritiesbyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('EconomicStatementID', models.IntegerField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
                ('SecurityName', models.CharField(blank=True, max_length=500)),
                ('SecutritySold', models.BooleanField()),
                ('AgencyNo', models.IntegerField(null=True)),
                ('CandidateDeleteSecurities', models.BooleanField()),
                ('DeleteRecord', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SourcesbyReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('PubOffNo', models.IntegerField()),
                ('AgencyNo', models.IntegerField(null=True)),
                ('EconomicStatementID', models.IntegerField()),
                ('SourceName', models.CharField(blank=True, max_length=255)),
                ('Director', models.BooleanField()),
                ('Officer', models.BooleanField()),
                ('Owner', models.BooleanField()),
                ('Member', models.BooleanField()),
                ('Partner', models.BooleanField()),
                ('Employer', models.BooleanField()),
                ('Employee', models.BooleanField()),
                ('Honorarium', models.BooleanField()),
                ('EmployerTerminated', models.BooleanField()),
                ('CandidateDelete', models.BooleanField()),
                ('DeleteRecord', models.BooleanField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('DateStart', officials.models.CFBDateTimeField()),
                ('DateEnd', officials.models.CFBDateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PrimaryRecID', models.IntegerField()),
                ('AgencyNo', models.IntegerField()),
                ('SubAgencyNo', models.IntegerField()),
                ('SubAgencyName', models.CharField(blank=True, max_length=100)),
                ('SAAddress', models.CharField(blank=True, max_length=100)),
                ('SAStreet', models.CharField(blank=True, max_length=50)),
                ('SACity', models.CharField(blank=True, max_length=50)),
                ('SAState', models.CharField(blank=True, max_length=15)),
                ('SAZip', models.CharField(blank=True, max_length=25)),
                ('SAContact', models.CharField(blank=True, max_length=100)),
                ('SATelephone', models.CharField(blank=True, max_length=30)),
                ('SAEmail', models.CharField(blank=True, max_length=75)),
                ('SAWebsite', models.CharField(blank=True, max_length=100)),
                ('SASenateConf', models.BooleanField()),
                ('SANeedsConf', models.BooleanField()),
                ('SAStatutcite', models.NullBooleanField()),
                ('SAAbolished', models.BooleanField()),
                ('SAbolishedDate', officials.models.CFBDateField(null=True)),
                ('SAuthority', models.NullBooleanField()),
                ('SAppointee', models.NullBooleanField()),
                ('Reporting_Cite', models.CharField(blank=True, max_length=50)),
                ('Establishment_Cite', models.CharField(blank=True, max_length=50)),
                ('SACertifiedDate', officials.models.CFBDateField(null=True)),
                ('SADisplayName', models.CharField(blank=True, max_length=100)),
                ('SAMemo', models.CharField(blank=True, max_length=255)),
                ('SAHas_Attachment', models.BooleanField()),
                ('SAAttachment', models.CharField(blank=True, max_length=255)),
                ('SASend_InterOffice_Mail', models.BooleanField()),
                ('Date_Entered', officials.models.CFBDateTimeField()),
                ('Last_Updated', officials.models.CFBDateTimeField()),
                ('msrepl_tran_version', models.CharField(blank=True, max_length=40)),
            ],
        ),
    ]
