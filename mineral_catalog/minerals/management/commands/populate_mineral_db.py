from django.core.management.base import BaseCommand
import json
from minerals.models import Mineral


class Command(BaseCommand):
    help = "Loads initial data from json file"

    source_file = 'data/minerals.json'

    fields = ['name', 'image caption', 'category', 'formula',
              'strunz classification', 'crystal system', 'unit cell',
              'color', 'crystal symmetry', 'cleavage', 'mohs scale hardness',
              'luster', 'streak', 'diaphaneity', 'optical properties',
              'group', 'refractive index', 'crystal habit', 'specific gravity']

    def handle(self, *args, **options):
        with open(self.source_file, encoding='UTF-8') as raw_data_file:
            raw_data = json.load(raw_data_file)

            for mineral in raw_data:
                for field in self.fields:
                    if field not in mineral:
                        mineral[field] = ''

                Mineral.objects.create(
                    name=mineral['name'],
                    image_caption=mineral['image caption'],
                    category=mineral['category'],
                    formula=mineral['formula'],
                    strunz_classification=mineral['strunz classification'],
                    crystal_system=mineral['crystal system'],
                    unit_cell=mineral['unit cell'],
                    color=mineral['color'],
                    crystal_symmetry=mineral['crystal symmetry'],
                    cleavage=mineral['cleavage'],
                    mohs_scale_hardness=mineral['mohs scale hardness'],
                    luster=mineral['luster'],
                    streak=mineral['streak'],
                    diaphaneity=mineral['diaphaneity'],
                    optical_properties=mineral['optical properties'],
                    group=mineral['group'],
                    crystal_habit=mineral['crystal habit'],
                    refractive_index=mineral['refractive index'],
                    specific_gravity=mineral['specific gravity']
                )

