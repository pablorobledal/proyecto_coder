from django.test import TestCase

from .models import CanaldeMensaje, CanaldeUsuario, Canal
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

class CanalTestCase(TestCase):
    def setUp(self):
        self.usuario_1=User.objects.create(username='juju1', password='asdasd1')
        self.usuario_2=User.objects.create(username='juju2', password='asdasd2')
        self.usuario_3=User.objects.create(username='juju3', password='asdasd3')

    def test_usuario_count(self):
        qs=User.Objetcs.all()
        self.assertEqual(qs.count(), 3)

    def test_cada_canaldeusuario(self):
        qs=User.Objetcs.all()
        for usuario in qs:
            canal_obj=Canal.objects.create
            canal_obj.usuarios.add(usuario)
        canal_qs=Canal.objects.all()
        self.assertEqual(canal_qs.count(), 3)
        canal_qs_1=canal_qs.solo_uno()
        self.assertEqual(canal_qs_1.count(), canal_qs.count())

    def prueba_dos_usuarios(self):
        canal_obj=Canal.objects.create()
        CanaldeUsuario.objects.create(usuario=self.usuario_1, canal=canal_obj)
        CanaldeUsuario.objects.create(usuario=self.usuario_2, canal=canal_obj)

        canal_obj2=Canal.objects.create()
        CanaldeUsuario.objects.create(usuario=self.usuario_3, canal=canal_obj2)

        qs=Canal.objects.all()
        self.assertEqual(qs.count(), 2)
        solo_dos=qs.solo_dos()
        self.assertEqual(solo_dos.count(), 1)

