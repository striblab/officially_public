import os

from django.conf import settings
from django.core.management.base import BaseCommand

from officials.models import *


class Command(BaseCommand):

    csv_dir = os.path.join(settings.BASE_DIR, 'data')

    def delete_existing(self):
        print("Deleting existing records...")
        CrossbyReport.objects.all().delete()
        EconomicStatement.objects.all().delete()
        HorseRacingbyReport.objects.all().delete()
        Position.objects.all().delete()
        Professional_ActivitybyReport.objects.all().delete()
        PublicOfficial.objects.all().delete()
        RealPropertyByReport.objects.all().delete()
        SecuritiesbyReport.objects.all().delete()
        SourcesbyReport.objects.all().delete()
        Agency.objects.all().delete()
        SubAgency.objects.all().delete()
        PositionType.objects.all().delete()

    def load_raw_tables(self):
        insert_count = PublicOfficial.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_PubOff.csv'))
        print("{} PubOff records inserted".format(insert_count))

        insert_count = EconomicStatement.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_EconomicStatement.csv'))
        print("{} EconomicStatement records inserted".format(insert_count))

        insert_count = Agency.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_agency.csv'))
        print("{} agency records inserted".format(insert_count))

        insert_count = SubAgency.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_subagency.csv'))
        print("{} subagency records inserted".format(insert_count))

        insert_count = Position.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_Position.csv'))
        print("{} Position records inserted".format(insert_count))

        insert_count = HorseRacingbyReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_HorseRacingbyReport.csv'))
        print("{} HorseRacingbyReport records inserted".format(insert_count))

        insert_count = Professional_ActivitybyReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_Professional_ActivitybyReport.csv'))
        print("{} Professional_ActivitybyReport records inserted".format(insert_count))

        insert_count = RealPropertyByReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_RealPropertyByReport.csv'))
        print("{} RealPropertyByReport records inserted".format(insert_count))

        insert_count = SecuritiesbyReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_SecuritiesbyReport.csv'))
        print("{} SecuritiesbyReport records inserted".format(insert_count))

        insert_count = SourcesbyReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_SourcesbyReport.csv'))
        print("{} SourcesbyReport records inserted".format(insert_count))

        insert_count = CrossbyReport.objects.from_csv(os.path.join(self.csv_dir, 'tbl_EIS_CrossbyReport.csv'))
        print("{} CrossbyReport records inserted".format(insert_count))

    def add_helper_fields(self):
        print("Finding unique PositionType combinations...")
        pts = []
        for unique_position in Position.objects.all().values('AgencyNo_id', 'SubAgencyNo_id', 'Title').distinct():
            # This is weird
            # if unique_position['SubAgencyNo_id'] == 0:
            #     subagency_id = None
            # else:
            #     subagency_id = unique_position['SubAgencyNo_id']

            pt = PositionType(
                agency_id=unique_position['AgencyNo_id'],
                subagency_id=unique_position['SubAgencyNo_id'],
                title=unique_position['Title'],
            )
            pts.append(pt)
        PositionType.objects.bulk_create(pts)

        print("{} PositionType records created. Assigning to Position records...".format(len(pts)))
        for pt in PositionType.objects.all():
            Position.objects.filter(AgencyNo=pt.agency, SubAgencyNo=pt.subagency, Title=pt.title).update(position_type=pt)

        print("Assigning Position records directly to officials for easier access...".format(len(pts)))
        for po in PublicOfficial.objects.all():
            po.gather_positions()

    def handle(self, *args, **kwargs):
        self.delete_existing()
        self.load_raw_tables()
        self.add_helper_fields()
