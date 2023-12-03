from apps.revisores.models import Revisor


def revisor_required(user):
    if Revisor.objects.filter(usuario=user).exists():
        return True
    return False