from django.db import models
from postgres_copy import CopyManager


class CFBDateTimeField(models.DateTimeField):
    copy_template = """
        CASE
            WHEN "%(name)s" = 'NA' THEN NULL
            ELSE to_timestamp("%(name)s", 'YYYY-MM-DD HH24:MI:SS')
        END
    """


class CFBDateField(models.DateField):
    copy_template = """
        CASE
            WHEN "%(name)s" = 'NA' THEN NULL
            ELSE to_date("%(name)s", 'YYYY-MM-DD')
        END
    """


class CFBIntegerField(models.IntegerField):
    copy_template = """
        CASE
            WHEN "%(name)s" = 'NA' THEN NULL
            ELSE "%(name)s"::INT
        END
    """


class CFBNAForeignKeyField(models.ForeignKey):
    copy_template = """
        CASE
            WHEN "%(name)s" = 'NA' THEN NULL
            ELSE "%(name)s"::INT
        END
    """


class CFBZeroForeignKeyField(models.ForeignKey):
    copy_template = """
        CASE
            WHEN "%(name)s" = '0' THEN NULL
            ELSE "%(name)s"::INT
        END
    """


class CFBNullBooleanField(models.NullBooleanField):
    copy_template = """
        CASE
            WHEN "%(name)s" = 'NA' THEN NULL
            ELSE "%(name)s"::BOOLEAN
        END
    """


class Agency(models.Model):
    PrimaryRecID = CFBIntegerField()
    AgencyNo = CFBIntegerField(primary_key=True)
    AName = models.CharField(max_length=255, blank=True)
    AAddress = models.CharField(max_length=100, blank=True)
    AStreet = models.CharField(max_length=50, blank=True)
    ACity = models.CharField(max_length=50, blank=True)
    AState = models.CharField(max_length=15, blank=True)
    AZip = models.CharField(max_length=25, blank=True)
    AContact = models.CharField(max_length=100, blank=True)
    ATelephone = models.CharField(max_length=30, blank=True)
    AEmail = models.CharField(max_length=75, blank=True)
    AWebsite = models.CharField(max_length=100, blank=True)
    SenateConf = models.BooleanField()
    NeedsConf = models.CharField(max_length=50, blank=True)
    Statutcite = models.CharField(max_length=50, blank=True)
    Reporting_Cite = models.CharField(max_length=50, blank=True)
    Establishment_Cite = models.CharField(max_length=50, blank=True)
    CertifiedDate = CFBDateField(null=True)
    Abolished = models.BooleanField()
    AbolishedDate = CFBDateField(null=True)
    Authority = models.CharField(max_length=100, blank=True)
    Appointee = models.CharField(max_length=50, blank=True)
    ADisplayName = models.CharField(max_length=100, blank=True)
    HasSubAgency = models.BooleanField()
    AHas_Attachment = models.BooleanField()
    AAttachment = models.CharField(max_length=255, blank=True)
    Memo = models.CharField(max_length=255, blank=True)
    ASend_InterOffice_Mail = models.BooleanField()
    Date_Entered = CFBDateTimeField()
    Last_Updated = CFBDateTimeField()
    msrepl_tran_version = models.CharField(max_length=40, blank=True)
    bySeat = models.BooleanField()
    objects = CopyManager()

    class Meta:
        ordering = ('AName',)

    def __str__(self):
        return self.AName


class SubAgency(models.Model):
    PrimaryRecID = CFBIntegerField()
    AgencyNo = models.ForeignKey(Agency, on_delete=models.CASCADE)
    SubAgencyNo = CFBIntegerField(primary_key=True)
    SubAgencyName = models.CharField(max_length=100, blank=True)
    SAAddress = models.CharField(max_length=100, blank=True)
    SAStreet = models.CharField(max_length=50, blank=True)
    SACity = models.CharField(max_length=50, blank=True)
    SAState = models.CharField(max_length=15, blank=True)
    SAZip = models.CharField(max_length=25, blank=True)
    SAContact = models.CharField(max_length=100, blank=True)
    SATelephone = models.CharField(max_length=30, blank=True)
    SAEmail = models.CharField(max_length=75, blank=True)
    SAWebsite = models.CharField(max_length=100, blank=True)
    SASenateConf = models.BooleanField()
    SANeedsConf = CFBNullBooleanField()
    SAStatutcite = CFBNullBooleanField()
    SAAbolished = models.BooleanField()
    SAAbolishedDate = CFBDateField(null=True)
    SAAuthority = CFBNullBooleanField()
    SAAppointee = CFBNullBooleanField()
    Reporting_Cite = models.CharField(max_length=50, blank=True)
    Establishment_Cite = models.CharField(max_length=50, blank=True)
    SACertifiedDate = CFBDateField(null=True)
    SADisplayName = models.CharField(max_length=100, blank=True)
    SAMemo = models.CharField(max_length=255, blank=True)
    SAHas_Attachment = models.BooleanField()
    SAAttachment = models.CharField(max_length=255, blank=True)
    SASend_InterOffice_Mail = models.BooleanField()
    Date_Entered = CFBDateTimeField()
    Last_Updated = CFBDateTimeField()
    msrepl_tran_version = models.CharField(max_length=40, blank=True)
    objects = CopyManager()

    class Meta:
        ordering = ('SubAgencyName',)


class PositionType(models.Model):
    ''' Created by strib to access similar positions in an agency '''
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    subagency = models.ForeignKey(SubAgency, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('title',)


class Position(models.Model):
    PrimaryRecID = CFBIntegerField()
    PositionNo = CFBIntegerField(primary_key=True)
    AgencyNo = models.ForeignKey(Agency, on_delete=models.CASCADE)
    SubAgencyNo = CFBZeroForeignKeyField(SubAgency, null=True, on_delete=models.CASCADE)
    Title = models.CharField(max_length=150, blank=True)
    AuthorityNo = CFBIntegerField(null=True)
    ByPosition = models.BooleanField()
    ByPositionNo = CFBIntegerField(null=True)
    ByPositionDesc = models.CharField(max_length=50, blank=True)
    MayDesignate = models.BooleanField()
    IsTempTitle = models.BooleanField()
    Designee_AuthNo = CFBIntegerField(null=True)
    temp_crossid = CFBIntegerField(null=True)
    SenateConf = models.BooleanField()
    NeedsConf = models.CharField(max_length=50, blank=True)
    Statutcite = models.CharField(max_length=50, blank=True)
    Reporting_Cite = models.CharField(max_length=50, blank=True)
    Establishment_Cite = models.CharField(max_length=50, blank=True)
    CountyID = CFBIntegerField(null=True)
    CandidateDistrict = models.CharField(max_length=5, blank=True)
    NumberSlots = CFBIntegerField(null=True)
    UnlimitedSlots = models.BooleanField()
    bySeat = models.BooleanField()
    Date_Entered = CFBDateTimeField()
    Last_Updated = CFBDateTimeField()
    msrepl_tran_version = models.CharField(max_length=40, blank=True)

    position_type = models.ForeignKey(PositionType, null=True, on_delete=models.SET_NULL)
    objects = CopyManager()


class PublicOfficial(models.Model):
    '''remember to use latin-1'''
    PrimaryRecID = CFBIntegerField()
    PubOffNo = CFBIntegerField(primary_key=True)
    SirName = models.CharField(max_length=10, blank=True)
    POFirstName = models.CharField(max_length=50, blank=True)
    POMI = models.CharField(max_length=5, blank=True)
    POLastName = models.CharField(max_length=50, blank=True)
    POSuffix = models.CharField(max_length=7, blank=True)
    POAddress = models.CharField(max_length=100, blank=True)
    POStreet = models.CharField(max_length=50, blank=True)
    POCity = models.CharField(max_length=50, blank=True)
    POState = models.CharField(max_length=15, blank=True)
    POZip = models.CharField(max_length=25, blank=True)
    POTelephone = models.CharField(max_length=30, blank=True)
    POEmail = models.CharField(max_length=75, blank=True)
    POOccupation = models.CharField(max_length=150, blank=True)
    POEmployer = models.CharField(max_length=150, blank=True)
    POBusAddr = models.CharField(max_length=150, blank=True)
    POBusStreet = models.CharField(max_length=50, blank=True)
    POBusCity = models.CharField(max_length=50, blank=True)
    POBusState = models.CharField(max_length=15, blank=True)
    POBusZip = models.CharField(max_length=25, blank=True)
    OldNo = models.CharField(max_length=10, blank=True)
    POBusSameAsHome = models.BooleanField()
    EIS_AnnualSent = models.BooleanField()
    EIS_AnnualSentDate = CFBDateTimeField(null=True)
    PreLastUpdate = CFBDateTimeField(null=True)
    POLastUpdate = CFBDateTimeField(null=True)
    RecentRecertDate = CFBDateTimeField(null=True)
    CandidateDelete = models.BooleanField()
    Send_InterOffice_Mail = models.BooleanField()
    hideProperty = models.BooleanField()
    WatershedID_Temp = CFBIntegerField(null=True)
    POHas_Attachment = models.BooleanField()
    POAttachment = models.CharField(max_length=255, blank=True)
    POMemo = models.CharField(max_length=255, blank=True)
    Waiver2ndHome = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    msrepl_tran_version = models.CharField(max_length=40, blank=True)
    MasterNameID = CFBIntegerField(null=True)
    StdAddressID = CFBNullBooleanField()
    AddressID = CFBNullBooleanField()

    positions = models.ManyToManyField(Position)
    position_types = models.ManyToManyField(PositionType)
    # agencies = models.ManyToManyField(Agency)

    objects = CopyManager()

    class Meta:
        ordering = ('POLastName', 'POFirstName')

    @property
    def display_name(self):
        middle_initial = ' {}'.format(self.POMI) if not 'NA' else ''
        return '{}{} {}'.format(self.POFirstName, middle_initial, self.POLastName)

    def gather_positions(self):
        for position in Position.objects.filter(crossbyreport__PubOffNo=self):
            self.positions.add(position)
            self.position_types.add(position.position_type)


class EconomicStatement(models.Model):
    EconomicStatementID = CFBIntegerField(primary_key=True)
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    OnlineApplicationIDs = models.CharField(max_length=255, blank=True)
    ScenarioType = models.CharField(max_length=30)
    StatementYear = CFBIntegerField(db_index=True)
    DueDate = CFBDateField()
    OriginalCertDate = CFBDateTimeField(null=True)
    AmendedDate = CFBDateTimeField(null=True)
    ProcessedDate = CFBDateTimeField(null=True)
    PrintedDate = CFBNullBooleanField()
    ElectronicFiler = models.BooleanField()
    Date_Entered = CFBDateTimeField()
    Last_Updated = CFBDateTimeField()
    objects = CopyManager()

    class Meta:
        ordering = ('-ProcessedDate',)


class HorseRacingbyReport(models.Model):
    PrimaryRecID = CFBIntegerField()  # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    InterestDesc = models.TextField()
    PartialInterest = models.BooleanField()
    FullInterest = models.BooleanField()
    Interest = models.TextField()
    AgencyNo = CFBNAForeignKeyField(Agency, null=True, on_delete=models.CASCADE)
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    objects = CopyManager()


class Professional_ActivitybyReport(models.Model):
    PrimaryRecID = CFBIntegerField()  # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    Professional_Activity = models.CharField(max_length=150, blank=True)
    Employee = models.BooleanField()
    Contractor = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    objects = CopyManager()

    def which_roles(self):
        roles = []
        for roletype in ['Employee', 'Contractor']:
            if getattr(self, roletype):
                roles.append(roletype)
        return ', '.join(roles)


class RealPropertyByReport(models.Model):
    PrimaryRecID = CFBIntegerField()  # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    Address = models.CharField(max_length=255, blank=True)
    Municipality = models.CharField(max_length=50, blank=True)
    County = models.CharField(max_length=75, blank=True)
    Acreage = models.CharField(max_length=75, blank=True)
    Fee = models.BooleanField()
    Mortgage = models.BooleanField()
    Contract = models.BooleanField()
    Option2500 = models.BooleanField()
    Option50000 = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    AgencyNo = CFBNAForeignKeyField(Agency, null=True, on_delete=models.CASCADE)
    CandidateDelete = models.BooleanField()
    objects = CopyManager()


class SecuritiesbyReport(models.Model):
    PrimaryRecID = CFBIntegerField()  # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    SecurityName = models.CharField(max_length=500, blank=True)
    SecutritySold = models.BooleanField()
    AgencyNo = CFBNAForeignKeyField(Agency, null=True, on_delete=models.CASCADE)
    CandidateDeleteSecurities = models.BooleanField()
    DeleteRecord = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    objects = CopyManager()

    class Meta:
        ordering = ('SecurityName',)


class SourcesbyReport(models.Model):
    PrimaryRecID = CFBIntegerField()   # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    AgencyNo = CFBNAForeignKeyField(Agency, null=True, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    SourceName = models.CharField(max_length=255, blank=True)
    Director = models.BooleanField()
    Officer = models.BooleanField()
    Owner = models.BooleanField()
    Member = models.BooleanField()
    Partner = models.BooleanField()
    Employer = models.BooleanField()
    Employee = models.BooleanField()
    Honorarium = models.BooleanField()
    EmployerTerminated = models.BooleanField()
    CandidateDelete = models.BooleanField()
    DeleteRecord = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    objects = CopyManager()

    class Meta:
        ordering = ('SourceName',)

    def which_roles(self):
        roles = []
        for roletype in ['Director', 'Officer', 'Owner', 'Member', 'Partner', 'Employer', 'Employee', 'Honorarium']:
            if getattr(self, roletype):
                roles.append(roletype)
        return ', '.join(roles)


class CrossbyReport(models.Model):
    PrimaryRecID = CFBIntegerField()  # No primary key?
    PubOffNo = models.ForeignKey(PublicOfficial, on_delete=models.CASCADE)
    EconomicStatementID = models.ForeignKey(EconomicStatement, on_delete=models.CASCADE)
    DateStart = CFBDateTimeField()
    DateEnd = CFBDateTimeField(null=True)
    AgencyNo = models.ForeignKey(Agency, on_delete=models.CASCADE)
    SubAgencyNo = CFBZeroForeignKeyField(SubAgency, null=True, on_delete=models.CASCADE)
    PositionNo = models.ForeignKey(Position, on_delete=models.CASCADE)
    POTitle = models.CharField(max_length=500, blank=True)
    DateReceived = CFBDateTimeField(null=True)
    Terminated = models.BooleanField()
    TerminationDate = CFBDateTimeField(null=True)
    ReAppoint = models.BooleanField()
    ReportIn = models.BooleanField()
    ReportInDate = CFBDateField(null=True)
    ApptDate = CFBDateField(null=True)
    TermEndDate = CFBDateField(null=True)
    PermStatus = models.BooleanField()
    Replaced = models.BooleanField()
    POLastReportFiled = CFBDateField(null=True)
    IsCandidate = models.BooleanField()
    CandType = models.CharField(max_length=25, blank=True)
    CandRegistrationNumber = CFBIntegerField(null=True)
    CandidateDelete = models.BooleanField()
    MoreThanOneBoard = models.BooleanField()
    TemporaryPublicOfficial = models.BooleanField()
    Last_Updated = CFBDateTimeField()
    Date_Entered = CFBDateTimeField()
    objects = CopyManager()

    class Meta:
        ordering = ('-DateReceived',)
