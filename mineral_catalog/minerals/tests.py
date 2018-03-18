from django.test import TestCase
from django.urls import reverse

# Create your tests here.

from .models import Mineral


class MineralsViewTests(TestCase):
    def setUp(self):
        self.test_mineral = Mineral.objects.create(
            name='Eliforesterite',
            image_caption='my very own self',
            category='human',
            formula='carbon, water, beer',
            strunz_classification='who?',
            crystal_system='lumpy',
            unit_cell='cell unit',
            color='pinkish',
            crystal_symmetry='right handed',
            cleavage='too much',
            mohs_scale_hardness='squishy',
            luster='gleaming',
            streak='wash',
            diaphaneity='ha',
            optical_properties='two',
            group='homo neanderthalensis'
        )

    def test_db(self):
        db_data = Mineral.objects.count()
        self.assertEqual(db_data, 1)

    def test_view_all(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertTemplateUsed('minerals/minerals.html')
        self.assertContains(resp, self.test_mineral.name)

    def test_view_detail(self):
        resp = self.client.get(reverse('minerals:detail',
                                       args=[self.test_mineral.pk]))
        self.assertTemplateUsed('minerals/mineral_detail.html')
        self.assertContains(resp, self.test_mineral.name)
        self.assertTrue(self.test_mineral.category in
                        resp.content.decode('UTF-8').lower())
        self.assertTrue(self.test_mineral.group in
                        resp.content.decode('UTF-8').lower())

    def test_view_random(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertTemplateUsed('minerals/mineral_detail.html')
        self.assertContains(resp, self.test_mineral.name)

