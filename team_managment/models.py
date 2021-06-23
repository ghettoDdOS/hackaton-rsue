from django.db import models


class Directions(models.Model):
    direction = models.CharField(max_length=100, verbose_name="Направление")

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"

    def __str__(self):
        return self.direction


class Teams(models.Model):
    team_name = models.CharField(max_length=100, verbose_name="Название")
    organization = models.CharField(max_length=100, verbose_name="Организация")
    direction = models.ForeignKey(Directions, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class Participants(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=30, verbose_name="Отчество")
    email = models.EmailField(verbose_name="E-mail")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (
            self.first_name,
            self.last_name,
        )

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"
