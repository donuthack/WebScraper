import datetime
import os
import re
import time

from cookie import authorization
import json
import requests
import xlsxwriter
import schedule
import datetime
import time


def removeNewDate(text):
    textWithoutNewDate = re.sub(re.compile('new Date(.*?)'), "", text).replace('(', '').replace(")", '')
    data = json.loads(textWithoutNewDate)
    return data


def listOfCars() -> None:
    all_cookies = authorization()

    global jar
    jar = requests.cookies.RequestsCookieJar()

    for cookie in all_cookies:
        jar.set(cookie.get('name'), cookie.get('value'))
    url_list_of_cars = 'https://www2.vauto.com/Va/Inventory/InventoryData.ashx'
    body = {
        'customSettings': '[{"id":"BlackBook_Wholesale","value":"0","condition":"Average","conditionLabel":"Average","type":"priceguide"},{"id":"KBBOnline_UCFPP_High","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_UCFPP_Low","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_UCFPP","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_TradeIn","value":"0","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_UCFPP_Diff","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_UCFPP_High_Diff","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"KBBOnline_UCFPP_Low_Diff","value":"1","condition":null,"conditionLabel":"None","type":"priceguide"},{"id":"Manheim_Wholesale","value":"0","condition":null,"conditionLabel":"None","type":"priceguide"}]',
        '_sortBy': 'LastListPriceChange ASC, DaysInInventory ASC',
        '_firstRecord': 0,
        'InventoryStatus': 0,
        'Historical': 0,
        'NewUsed': 'U',
        'ExcludeFromCounts': 0,
        'HqTranferEntityNotSame': False,
        'RetailWholesale': 'R',
        'gridSrcName': 'inventoryDetail',
        '_pageSize': 2500
    }
    response = requests.post(url_list_of_cars, data=body, cookies=jar)
    result = removeNewDate(response.text)
    carInfo(result)
    # return result


def carInfo(struct):
    today = datetime.datetime.now()
    for car in struct.get('rows'):
        # print(37, car[3], "|", car[6], "|", "RetailWholesale", car[22], "|", "DaysInInventory", car[43], "|", "Vin",
        #       car[13], "|", "StockNumber", car[12], "|", "ModelYear", car[7], "|", "Make", car[8], "|", "Model", car[9],
        #       "|", "Series", car[10], "|", "Odometer", car[24], "|", "BodyDescription", car[18], "|",
        #       "EngineDescription", car[73], "|", "TransmissionDescription", car[160], "|", "DriveTrainType", car[70],
        #       "|", "ExteriorColor", car[164], "|", "InteriorColor", car[21], "|", "Title", car[6], "|", "Id", car[0],
        #       "|", "DealerId", car[2], "|", "MarketingImageSetId", car[156], "|", "VehicleType", car[63])
        if car[49] != "None" and car[3] != '1st Gear Auto Inc':
            post_data = {
                "Vehicle": {
                    "RetailWholesale": car[22],
                    "DaysInInventory": car[43],
                    "Vin": car[13],
                    "StockNumber": car[12],
                    "ModelYear": car[7],
                    "Make": car[8],
                    "Model": car[9],
                    "Series": car[10],
                    "Odometer": car[24],
                    "BodyDescription": car[18],
                    "EngineDescription": car[73],
                    "TransmissionDescription": car[160],
                    "DriveTrainType": car[70],
                    "ExteriorColor": car[164],
                    "InteriorColor": car[21],
                    "Title": car[6],
                    "Id": car[0],
                    "DealerId": car[2],
                    "MarketingImageSetId": car[156],
                },
                "CompetitiveSet": {
                    "Ranks": []
                },
                "ShowAllColumns": True
            }
            data = json.dumps(post_data)
            headers = {
                "Content-Type": "application/json"
            }
            url = "https://www2.vauto.com/Va/Ranking/Ranking.ashx?action=ranking&IncludeMyVehicle=&initialLoad=true"
            response = requests.post(url, data=data, headers=headers, cookies=jar)
            print("Response", response)
            responseFromNode = requests.post('http://localhost:3000/test', data={'text': response.text})
            print("Response From Node", responseFromNode)
            result = removeNewDate(responseFromNode.text)
            createExcel(result, today)


def createExcel(result, fileName):
    print("Create Excel")
    labels = ["Rank", "VRank", "Make/Model", "VIN", "Stock#", "Certified", "Body", "Interior", "Color",
              "Engine", "Transmission", "DriveTrain", "Price", "Odometer", "Age", "Distance", "Seller",
              "SellerAddress", "SellerCity", "SellerState", "SellerPostalCode", "CARFAX 1-Owner",
              "CARFAX 1-OwnerReportOnline", "CARFAX CleanTitle"]

    vin = result['Vehicle']['Vin']
    stock = result['Vehicle']['StockNumber']
    distance = result["CompetitiveSet"]["Distance"]

    millisecond = datetime.datetime.now()
    timestamp = time.mktime(millisecond.timetuple()) * 1000

    rows = result["CompetitiveSet"]['CompetitiveVehicles']['Rows']
    workbook = xlsxwriter.Workbook(
        "C:\\vAuto\\Unprocessed\\AutoCompSet_{0}_{1}_{2}_{3}.xlsx".format(str(vin), str(stock), str(distance),
                                                                          str(timestamp)))
    worksheet = workbook.add_worksheet()

    colLables: int = 0

    for label in labels:
        worksheet.write(0, colLables, label)
        colLables += 1

    row = 1
    col = 0

    for auto in rows:
        worksheet.write(row, 0, auto[4])  # Rank
        worksheet.write(row, 1, auto[5])  # VRank
        worksheet.write(row, 2, auto[10])  # MakeModel
        worksheet.write(row, 3, auto[37])  # VIN
        worksheet.write(row, 4, None)  # Stock
        worksheet.write(row, 5, auto[23])  # Certified
        worksheet.write(row, 6, auto[11])  # Body
        worksheet.write(row, 7, auto[2])  # Interior
        worksheet.write(row, 8, auto[1])  # Color
        worksheet.write(row, 9, auto[12])  # Engine
        worksheet.write(row, 10, auto[13])  # Transmission
        worksheet.write(row, 11, auto[14])  # Drive train
        worksheet.write(row, 12, auto[34])  # Price
        worksheet.write(row, 13, auto[35])  # Odometer
        worksheet.write(row, 14, auto[3])  # Age
        worksheet.write(row, 15, auto[6])  # Disntance
        worksheet.write(row, 16, auto[16])  # Seller
        worksheet.write(row, 17, auto[17])  # Seller Address
        worksheet.write(row, 18, auto[18])  # Seller City
        worksheet.write(row, 19, auto[19])  # Seller State
        worksheet.write(row, 20, auto[20])  # Seller Postal Code
        worksheet.write(row, 21, auto[24])  # CARFAX 1-Owner
        worksheet.write(row, 22, auto[26])  # CARFAX 1-Owner Report Online
        worksheet.write(row, 23, auto[25])  # CARFAX Clean Title
        row += 1

    workbook.close()
    print("Close XLSX")


schedule.every().day.at("02:40").do(listOfCars)
while True:
    schedule.run_pending()
    time.sleep(1)
