from schemas import ProductCreateSchema2
from schemas import ProductCreateSchema


def get_products_data() -> list[ProductCreateSchema2]:
    
    rb265 = ProductCreateSchema2(
        company_id=1,
        type_id=1,
        name="RoadBase 265",
        description="adgezive additive for sintez road chemical",
        )

    uba111 = ProductCreateSchema2(
        name="UniBase A111",
        description="MUE 93% + MA 7%",
        company_id=1,
        type_id=2,
        )

    drodure = ProductCreateSchema2(
        name="Drocure 5910",
        description="Indian name of Basf AMIX1000",
        company_id=7,
        type_id=2,
        )

    amdor31t = ProductCreateSchema2(
        name="Amdor 31T",
        description="from Amdor production road-emulsifer",
        company_id=2,
        type_id=1,
        )

    eahighers = ProductCreateSchema2(
        name="EA_HIGHERS",
        description="Highers ethylen amine from Saudi Arabia",
        company_id=4,
        type_id=1,
        )

    return [rb265, uba111, drodure, amdor31t, eahighers]