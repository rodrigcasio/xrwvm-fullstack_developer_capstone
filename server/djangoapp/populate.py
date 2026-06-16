from .models import CarMake, CarModel


def initiate():
    # 1. Create CarMake instances
    makes = {
        "NISSAN": "Japanese", "Mercedes": "German",
        "Audi": "German", "Kia": "Korean", "Toyota": "Japanese"
    }
    make_objs = {}
    for name, tech in makes.items():
        make_objs[name] = CarMake.objects.create(
            name=name,
            description=f"Great cars. {tech} technology"
        )

    # 2. Create CarModel instances with dealer_id=1
    models = [
        ("Pathfinder", "SUV", 2023, make_objs["NISSAN"]),
        ("Qashqai", "SUV", 2023, make_objs["NISSAN"]),
        ("XTRAIL", "SUV", 2023, make_objs["NISSAN"]),
        ("A-Class", "SUV", 2023, make_objs["Mercedes"]),
        ("C-Class", "SUV", 2023, make_objs["Mercedes"]),
        ("E-Class", "SUV", 2023, make_objs["Mercedes"]),
        ("A4", "SUV", 2023, make_objs["Audi"]),
        ("A5", "SUV", 2023, make_objs["Audi"]),
        ("A6", "SUV", 2023, make_objs["Audi"]),
        ("Sorrento", "SUV", 2023, make_objs["Kia"]),
        ("Carnival", "SUV", 2023, make_objs["Kia"]),
        ("Cerato", "Sedan", 2023, make_objs["Kia"]),
        ("Corolla", "Sedan", 2023, make_objs["Toyota"]),
        ("Camry", "Sedan", 2023, make_objs["Toyota"]),
        ("Kluger", "SUV", 2023, make_objs["Toyota"]),
    ]

    for name, m_type, year, make in models:
        CarModel.objects.create(
            name=name, type=m_type, year=year,
            car_make=make, dealer_id=1
        )
