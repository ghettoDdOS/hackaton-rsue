from django.db import models


class CoreSettings(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название мероприятия",
    )
    sub_title = models.CharField(
        max_length=255,
        verbose_name="Подзаголовок",
    )
    format_type = models.CharField(
        max_length=255,
        verbose_name="Формат проведения",
    )
    date = models.CharField(
        max_length=255,
        verbose_name="Дата проведения",
    )
    registration = models.BooleanField(
        verbose_name="Открыть/закрыть регистрацию",
        help_text="По умолчанию открыта",
        default=True,
    )
    video_link = models.URLField(
        verbose_name="Ссылка на трансляцию",
        help_text="Ссылка из iframe на youtube",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Основные настройки"
        verbose_name_plural = "Основные настройки"

    @staticmethod
    def get_instance():
        return CoreSettings.objects.get_or_create(pk=0)

    def __str__(self):
        return "Основные настройки"


class Document(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Наименование",
    )
    file = models.FileField(
        verbose_name="Документ",
        null=True,
        blank=True,
        upload_to="static/doc",
    )
    order = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="Порядок вывода",
    )

    class Meta:
        ordering = ("order",)
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.name


class Dates(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
    )
    date = models.DateField(
        verbose_name="Дата проведения",
    )

    class Meta:
        ordering = ("date",)
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.name


class Sponsors(models.Model):
    name = models.CharField(max_length=100, verbose_name="Спонсор")
    logo = models.ImageField(
        upload_to="static/image/footer-logo", verbose_name="Логотип"
    )
    link = models.URLField(
        max_length=255,
        verbose_name="Ссылка",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Спонсор"
        verbose_name_plural = "Спонсоры"

    def __str__(self):
        return self.name


class Case(models.Model):
    case_name = models.CharField(max_length=100, verbose_name="Название")
    caseholder = models.ForeignKey(
        Sponsors,
        on_delete=models.CASCADE,
        verbose_name="Спонсор",
        blank=True,
        null=True,
    )
    tasks = models.TextField(
        verbose_name="Задачи",
    )

    def __str__(self):
        return self.case_name

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"
