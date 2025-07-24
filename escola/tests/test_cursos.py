from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso


class CursosTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(
            username="admin", password="admin", email="admin@gmail.com"
        )
        self.url = reverse("Cursos-list")
        self.client.force_authenticate(self.usuario)

        self.curso_01 = Curso.objects.create(
            codigo="1", descricao="Rocketseat", nivel="I"
        )
        self.curso_02 = Curso.objects.create(codigo="2", descricao="Alura", nivel="A")

    def test_requisicao_get_para_listar_cursos(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
