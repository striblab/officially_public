import os

from django.conf import settings
from django.core.management.base import BaseCommand

from officials.models import *


class Command(BaseCommand):

    csv_dir = os.path.join(settings.BASE_DIR, 'data', 'legislator_honoraria.csv')

    def handle(self, *args, **kwargs):
        honoraria = SourcesbyReport.objects.filter(
            Honorarium=True,
            EconomicStatementID__DueDate__gte='2020-01-01',
            EconomicStatementID__crossbyreport__AgencyNo__AName__in=['Senate', 'House of Representatives']
        ).distinct()

        for report in honoraria:
            print(report.PubOffNo.POLastName, report.PubOffNo.POFirstName, report.SourceName)
