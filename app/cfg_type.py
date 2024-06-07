from schemas import TypeCreateSchema


def get_type_data() -> list[TypeCreateSchema]:
    
    adgeziv = TypeCreateSchema(
        name="adgezive",
        description="adgezive and other info",
        )

    corrozive = TypeCreateSchema(
        name="corrosia",
        description="MUE 93% + MA 7%",
        )

    epoxyde = TypeCreateSchema(
        name="cpoxyde",
        description="epoxyd and other info",
        )

        
    return [adgeziv, corrozive, epoxyde]
