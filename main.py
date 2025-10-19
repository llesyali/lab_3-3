import os
import django



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lab3.settings")
django.setup()

from main.repositories.repomanager import Repository_manager
def main():
    repository_manager = Repository_manager()
    while True:
        number=int(input("Enter the number of the action: "))
        id=4

        match number:
                case 1:
                    person = repository_manager.company.create({
                        "name_company": "klass",
                        "contact": "0971598771",
                        "email": "liashkolesya@gmail.com",
                        "locality_address": "Dubrovytsia",
                        "street_address": "Shevchenka",
                        "house_number": "89"
                    })
                    print(f"{person.name_company} is created")
                case 2:

                    delit=repository_manager.company.delete(id)
                    if delit:
                        print(f"{delit.name_company} is deleted")
                    else :
                        print("error")
                case 3:
                    find = repository_manager.ticket.get_by_id(id)
                    if find:
                        print(f"Ticket {find.ticket_id} with price {find.price} is found")
                    else:
                        print("Ticket not found")
                case 4:
                    for t in repository_manager.stop.get_all():
                        print(f'{t.name} - {t.street}')
                case 5:
                    for t in repository_manager.director.get_all():
                        print(f'{t.name} - {t.contact}')

if __name__ == "__main__":
    main()
