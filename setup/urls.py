from django.contrib import admin
from django.urls import path, include
from escola.views import (
    EstudanteViewSet,
    CursoViewSet,
    ListaMatriculaCurso,
    MatriculaViewSet,
    ListaMatriculaEstudante,
)
from rest_framework import routers


router = routers.DefaultRouter()
router.register("estudantes", EstudanteViewSet, "Estudantes")
router.register("cursos", CursoViewSet, "Cursos")
router.register("matriculas", MatriculaViewSet, "Matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("estudantes/<int:pk>/matriculas/", ListaMatriculaEstudante.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaMatriculaCurso.as_view()),
]
