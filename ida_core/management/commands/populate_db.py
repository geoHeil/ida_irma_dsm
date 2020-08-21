from django.core.management.base import BaseCommand
from ida_core.models import AccessModeType, AccessModeAnonymization, AccessModeResearchField, ResearcherType

class Command(BaseCommand):
    help = 'Fill the database with (very limited) test data'

    def _create_test_data(self):
        AccessModeType(name='Secure on-site access',description='Provision in the premises of the institution in a dedicated secure environment.').save()
        AccessModeType(name='On-site access',description='Provision via the institutions IT infrastructure.').save()
        AccessModeType(name='Remote execution',description='Researcher sends code and RDC sends back results.').save()
        AccessModeType(name='On-site in partner institution',description='On-site access in partner institution.').save()
        AccessModeType(name='Remote on-site access',description='Remote access for internal researchers (e.g. teleworking).').save()
        AccessModeType(name='Remote access',description='Researcher can access data remotely from own institution.').save()
        AccessModeType(name='Download',description='Scientific use files or public use files.').save()
        AccessModeAnonymization(name='Non-anonymized',description='No anonymization (i.e. raw data).').save()
        AccessModeAnonymization(name='Formal anonymization',description='Deletion of direct identifiers such as names, addresses, and other identifiers (e.g. LEI). No direct identification possible (i.e. secure use files).').save()
        AccessModeAnonymization(name='Factual anonymization',description='Identification only with significant effort possible (i.e. scientific use files).').save()
        AccessModeAnonymization(name='Perturbed data',description='Data modified using statistical methods.').save()
        AccessModeAnonymization(name='Full anonymization',description='No identification possible (i.e. public use files).').save()
        AccessModeResearchField(name='Any field',description='Any field').save()
        AccessModeResearchField(name='Scientific research',description='Scientific research').save()
        AccessModeResearchField(name='Monetary policy',description='Monetary policy').save()
        AccessModeResearchField(name='Tasks of the ESCB',description='Exercise of the tasks of the ESCB').save()
        ResearcherType(name='Internal').save()
        ResearcherType(name='External').save()
        print('Finished populating database.')

    def handle(self, *args, **options):
        self._create_test_data()
