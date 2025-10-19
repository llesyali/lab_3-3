from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:

    def __init__(self, model):
        self.model = model


    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, id):
        try:
            return self.model.objects.get(pk=id)
        except ObjectDoesNotExist:
            return None


    def create(self, data):
        return self.model.objects.create(**data)

    def delete(self, id):
        some=self.get_by_id(id)
        if some:
            some.delete()
            return some
        else:
            return None

    def update(self,id, data):
        some=self.get_by_id(id)
        if some:
            for k, v in data.items():
                setattr(some, k, v)
            some.save()
            return some
