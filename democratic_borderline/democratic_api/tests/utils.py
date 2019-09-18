from democratic_api.models import Nationality


class DataBaseSetupMixin:
    def set_up_database(self):
        for nationality in ("ukrainian", "british", "tai"):
            nationality = Nationality.objects.create(nationality=nationality)
            nationality.save()
        self.db_default_nationality = Nationality.objects.first().pk
