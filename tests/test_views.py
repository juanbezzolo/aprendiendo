from django.test import TestCase
from django.urls import reverse
from core.models import Usuarios


class IndexViewTests(TestCase):
    def setUp(self):
        Usuarios.objects.create(nombre='Juan', correo='juan@example.com', rol='Admin')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Sistema de cultivo')

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Iniciar sesión')
