import pymysql


class Donor:
    def __init__(self, name, blood_group, phone, cnic, city):
        self.name = name
        self.blood_group = blood_group
        self.phone = phone
        self.cnic = cnic
        self.city = city


DB_CONFIG = {
    "host": "localhost",
    "user": "faatehsultan",
    "password": "khalliwalli",
    "database": "blood_db"
}

try:
    db = pymysql.connect(
        host=DB_CONFIG['host'], user=DB_CONFIG['user'],
        password=DB_CONFIG['password'], database=DB_CONFIG['database']
    )
    dbCur = db.cursor()
except:
    print("Error: Cannot Establish Connection to the Database!")


def insertDonor(donor):
    query = f"INSERT INTO donors (`name`, `blood group`, `phone`, `cnic`, `city`) VALUES ('{donor.name}','{donor.blood_group}','{donor.phone}','{donor.cnic}', '{donor.city}');"
    print(query)
    try:
        dbCur.execute(query)
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False


def searchDonor(name = None, blood_group = None, phone = None, city = None):
    query = "SELECT * FROM donors"
    if name or phone or blood_group or city:
        query += " where "
    if name:
        query += f" name like '%{name}%'"
    if phone:
        if name:
            query += " OR "
        query += f" phone like '{phone}%'"
    if blood_group:
        if phone:
            query += " OR "
        query += f" `blood group` = '{blood_group}'"
    if city:
        if blood_group:
            query += " OR "
        query += f" city = '%{city}%'"
        
    try:
        dbCur.execute(query)
        queryResult = dbCur.fetchall()
        donorList = []
        for q in queryResult:
            donorList.append(
                Donor(
                    q[1], q[2], q[3], q[4], q[5]
                )
            )
        return donorList
    except Exception as e:
        print(e)