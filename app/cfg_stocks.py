from schemas import StockCreateSchema2




def get_data_of_stocks() -> list[StockCreateSchema2]:

    stock1 = StockCreateSchema2(
        weight=10.5,
        description="some desctiption",
        price=470_000,
        company_id=1,
        product_id=1,
    )
    stock2 = StockCreateSchema2(
        weight=150,
        description="amine from dubae",
        price=360_000,
        company_id=1,
        product_id=5,
    )
    stock3 = StockCreateSchema2(
        weight=17.6,
        description="droducre == amix1000",
        price=500_000,
        company_id=1,
        product_id=3,
    )
    stock4 = StockCreateSchema2(
        weight=10.5,
        description="our production",
        price=470_000,
        company_id=1,
        product_id=2,
    )

    return [stock1, stock2, stock3, stock4]