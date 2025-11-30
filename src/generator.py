import saver
import uuid
import random
import uuid
from typing import List
from datetime import date, timedelta

def generate_account_data(username: str | None, api_id: str | None) -> dict:
    data = {
        "uuid": str(uuid.uuid4()),
        "username": username if username else "mock_user_" + str(random.randrange(1000, 9999)),
        "status": 1,
        "joined": "2019-10-12T20:41:52.400299",
        "lastLogin": "2020-08-15T13:43:17.607111",
        "permissions": {
            "civilian": True,
            "lawyer": True,
            "dmv": True,
            "police": True,
            "fire": True,
            "ems": True,
            "dispatch": True,
            "admin": True,
            "polRecAdd": True,
            "polRecEdit": True,
            "polRecRemove": True,
            "polSuper": True,
            "polEditUnit": True,
            "polEditOtherUnit": True,
            "selfDispatch": True,
            "medRecAdd": True,
            "medRecEdit": True,
            "medRecRemove": True,
            "medSuper": True,
            "fireRecAdd": True,
            "fireRecEdit": True,
            "fireRecRemove": True,
            "fireSuper": True,
            "dmvRecAdd": True,
            "dmvRecEdit": True,
            "dmvRecRemove": True,
            "dmvSuper": True,
            "lawRecAdd": True,
            "lawRecEdit": True,
            "lawRecRemove": True,
            "lawSuper": True,
            "adminAccounts": True,
            "adminPermissionKeys": True,
            "adminCustomization": True,
            "adminDepartments": True,
            "adminTenCodes": True,
            "adminPenalCodes": True,
            "adminInGameIntegration": True,
            "adminDiscordIntegration": True,
            "adminLimits": True,
            "adminLogs": True
        },
        "apiIds": [
            api_id if api_id else str(random.randrange(100000, 999999))
        ]
    }
    return data

def generate_cad_character(name: str | None = None, username: str | None = None, api_id: str | None = None) -> dict:
    first_names = ["John", "Jane", "Alice", "Bob", "Michael", "Sara", "Tom"]
    last_names = ["Doe", "Smith", "Johnson", "Brown", "Taylor", "Davis", "Miller"]

    if name and " " in name:
        first_name, last_name = name.split(" ", 1)
    else:
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"

    # Calculate birth date and age
    age = random.randint(18, 50)
    birth_date = date.today() - timedelta(days=age*365 + random.randint(0, 364))
    birth_date_str = birth_date.strftime("%d/%m/%Y")

    def random_phone() -> str:
        return f"+1 {random.randint(200, 999)} - {random.randint(100, 999)} - {random.randint(1000, 9999)}"

    def make_field(
        field_type, label, value="", size=4, options=None, uid=None,
        isPreviewed=False, isSupervisor=False, isRequired=True, unique=False,
        readOnly=False, mask=""
    ):
        return {
            "type": field_type,
            "label": label,
            "value": value,
            "size": size,
            "data": {},
            "options": options or [],
            "isPreviewed": isPreviewed,
            "isSupervisor": isSupervisor,
            "isRequired": isRequired,
            "unique": unique,
            "readOnly": readOnly,
            "mask": mask,
            "maskReverse": False,
            "dbMap": True,
            "isFromSync": False,
            "uid": uid or str(uuid.uuid4()),
            "dependency": {"type": None, "fid": None, "acceptableValues": None}
        }

    sections = [
        {
            "category": 0,
            "label": "Fotka",
            "fields": [
                make_field("image", "VAŠE FOTKA ZDE", value="", size=12, uid="img")
            ],
            "searchCiv": False,
            "searchVeh": False,
            "enableDuplicate": False,
            "isDuplicate": False,
            "dependency": {"type": None, "fid": None, "acceptableValues": None}
        },
        {
            "category": 0,
            "label": "Civilista",
            "fields": [
                make_field("text", "Křestní jméno", first_name, size=4, isPreviewed=True, uid="first"),
                make_field("text", "Příjmení", last_name, size=3, isPreviewed=True, uid="last"),
                make_field("date", "Datum narození", birth_date_str, size=5, mask="DD/MM/YYYY", uid="dob"),
                make_field("text", "Věk", str(age), size=2, isPreviewed=True, mask="##", uid="age"),
                make_field("select", "Pohlaví", "", size=3, options=["MUŽ","ŽENA"], uid="sex"),
                make_field("text", "Bydliště", f"{random.randint(100,999)} Main St", size=7, uid="residence"),
                make_field("text", "Postal kód", f"{random.randint(10000,99999)}", size=4, uid="zip"),
                make_field("text", "Výška", str(random.randint(150,200)), size=2, uid="height"),
                make_field("text", "Váha", str(random.randint(50,100)), size=2, uid="weight"),
                make_field("select", "Pleť", "", size=4, options=["ČERNÁ","BÍLÁ","ŽLUTÁ"], uid="skin"),
                make_field("select", "Barva vlasů", "", size=6, options=["BLOND","BRUNET","ZRZAVÉ","ČERNÁ","BÍLÁ","MODRÁ","ŽÁDNÉ VLASY"], uid="hair"),
                make_field("select", "Barva očí", "", size=6, options=["ZELENÁ","MODRÁ","HNĚDÁ"], uid="eyes"),
                make_field("text", "Vztah", "Single", size=6, uid="emergencyRelationship"),
                make_field("text", "Telefonní číslo", random_phone(), size=6, isSupervisor=True, readOnly=True, mask="+1 ### - ### - ####", uid="phone_number"),
                make_field("text", "discord nick", "", size=6, uid="_jrq6awj6y"),
                make_field("text", "discord id", "", size=6, uid="_052n0nc8b")
            ],
            "searchCiv": False,
            "searchVeh": False,
            "enableDuplicate": False,
            "isDuplicate": False,
            "dependency": {"type": None, "fid": None, "acceptableValues": None}
        }
    ]

    cad_character = {
        "recordTypeId": 7,
        "id": random.randint(1000,9999),
        "syncUniqueId": None,
        "syncId": "",
        "name": name,
        "img": None,
        "type": 7,
        "sections": sections,
        "username": username if username else "mock_user_" + str(random.randrange(1000, 9999)),
        "apiIds": [api_id if api_id else str(random.randrange(100000, 999999))]
    }

    return cad_character