from schemas import CompanyCreateSchema

def get_list_companies():
    horda = CompanyCreateSchema(
        name="Horda",
        city="Saint-Petersburg",
        inn=7813299598,
        kpp=781301001,
        address="197022, gorod Sankt-Peterburg, ul CHapygina, d. 6 litera P, ofis 214, r.m. 1",
        phone=79999999999,
        email="ivan_lo@hordanpp.com"
    )

    amdor = CompanyCreateSchema(
        name="Amdor",
        city="N-Tagil",
        inn=6623024667,
        kpp=662301001,
        address="622051, Sverdlovskaya oblast', gorod Nizhnij Tagil, Severnoe sh., d.21",
        phone=75555555555,
        email="amdor@ucp.ru",
    )

    sinteztnp = CompanyCreateSchema(
        name="SintezTNP",
        city="Ufa",
        inn=277003925,
        kpp=27701001,
        address="450029, RESPUBLIKA BASHKORTOSTAN, G. UFA, UL. YUBILEJNAYA, D.5",
        phone=72222222222,
        email="sintez@tnp.ru",
    )

    diks = CompanyCreateSchema(
        name="Diks",
        city="Saint-Petersburg",
        inn=7802327116,
        kpp=780601001,
        address="195030, G.SANKT-PETERBURG, UL. HIMIKOV, D. 28, LITER AS, POMESHCH. 906",
        phone=77777777777,
        email="info@diks-spb.ru",
    )

    euroline = CompanyCreateSchema(
        name="EurolineTrading",
        city="Saint-Petersburg",
        inn=7805450679,
        kpp=784201001,
        address="g. Sankt-Peterburg, ul. SHpalernaya, d. 51, lit. A, pom. 2-N, kom. 296",
        phone=73333333333,
        email="info@etldr.ru",
    )
    itps = CompanyCreateSchema(
        name="ITPS",
        city="Kazan",
        inn=1660043700,
        kpp=166001001,
        address="g. Kazan', ul. Nikolaya Ershova, d. 35a, pom. 46-50, et. 2",
        phone=74444444444,
        email="kazan@itps.ru",
    )
    
    omea = CompanyCreateSchema(
        name="Omea Algol rus",
        city="Moscow",
        inn=7816108883,
        kpp=770501001,
        address="g. Moskva, vn.ter.g. municipal'nyj okrug Zamoskvorech'e, Kosmodamianskaya nab., d. 52, str. 4",
        phone=71111111111,
        email="111@omea.ru",
    )

    return [horda, amdor, sinteztnp, diks, euroline, itps, omea]