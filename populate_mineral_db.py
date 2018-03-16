import json
from mineral_catalog.minerals.models import Mineral


class LoadData():
    file = 'data/minerals.json'

    def initial_load(apps, schema_editor):
        source_file = 'data/minerals.json'
        with open(source_file, encoding='UTF-8') as raw_data_file:
            raw_data = json.load(raw_data_file)
            fields = ['name', 'image filename', 'image caption', 'category',
                      'formula', 'strunz classification', 'crystal system',
                      'unit cell', 'color', 'crystal symmetry', 'cleavage',
                      'mohs scale hardness', 'luster', 'streak', 'diaphaneity',
                      'optical properties', 'group']

            for mineral in raw_data:

                for field in fields:
                    if field not in mineral:
                        mineral[field] = ''

                new_mineral = Mineral.objects.create(
                    name=mineral['name'],
                    image_filename=mineral['image filename'],
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
                    group=mineral['group']
                )


if __name__ == '__main__':
    a = LoadData()
    a.initial_load()
