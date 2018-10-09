from django.db import models

class Agencia(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Agencia"
        verbose_name_plural = "Agencias"

    def __str__(self):
        return self.nome


class Depoimentos(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    depoimento = models.CharField(max_length=900)

    class Meta:
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.nome


class Psicologo(models.Model):
    nome = models.CharField(max_length=255)
    contato = models.CharField(max_length=255)
    agencia = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Psicologo"
        verbose_name_plural = "Psicologos"

    def __str__(self):
        return self.nome
