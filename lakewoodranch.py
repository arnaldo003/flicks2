import requests
from bs4 import BeautifulSoup
import pandas
import gspread
import numpy as np
import datetime

class lakewood:
    
    creds = {
        "type": "service_account",
        "project_id": "crypto-messari",
        "private_key_id": "9cd2f9d784c4baaba89c4f5f8a565ac47d2b33ab",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCwQ2KpOgPnA7wv\nuBjzFYbkL8vmfuFlQ1e3j8IqG0Ikale7bWfc24E21cK4ZX1zeCbN5R4Rcb560q4L\nLTiLLvsfcZYyh+WCtdih//Jdg7LelwejNP8FemVy5eXvtaWJVLIVw7XDDLxA34dQ\nXrtTECiiT4cZ4S+m/Pt7m6h8e1f3ddrKbAjr91vq6gWlY0x5bIJwvjoc8jkcKzpj\ndQ6VBa6SHjQ2X4qUUEzxflpDh+qbgXm208VBr/sMfwtzueL+F9NmvJ3jSkF/Ahjl\nSNPuKXY6TbwqS+oaPf7mFQRsvXTJ0o7skVLqsoOEsAYd1DDV12usKZaQV35CUh/p\nmSvG9+k5AgMBAAECggEALQO4kaFIV9ojWEh6zrHDtkjimOX0aCkPoMhs/NXjSWuD\nJlGlgcjpMfjbdr4skK2xs0l9KVVUIQfm/OG6nAkOhxQ6GIOOQJhyT8UOv4UfzCrj\n/3FMY7jDadl+pH5OXUktBdPqenqpJSQw6XyX+Hma9wC6bwiMY+gdzY6OM+RILeEV\nc58YvulFxSHAwmb5voh5SEalnnC4G3dO3qOwBaMRzNmEpSs9OIDWQ4/BKCrvViyI\ntcpHgCt/d9AtiU61k1GxJzFiiJt/Pu5abmfnvQhZcLrhG9rkoO4dZ1zvbKKYUzgk\nZkw3Yt1Xk3y34S5rl42XsVOmNAeaRkIy/ZoqDTLZ9QKBgQDm5mWV3Awb5iJjj3C5\n/jigoxLWuBiHkBEQg7krjnStBaAOms1fIWBUP6mw5cBH+BM17uij8c1eqRT3HVwZ\n0j+qQKbd65erMtlmOYucUJSbWcX/kEXIfXEYP+hAmSTAuir8Eqgtu0V7jgpa5ffH\npweCn9Pf1lzckKwqhCT709IrxwKBgQDDbIdamsk85GgZcvaXuEYptg3sVTKsksuV\n7+hymV7sC2zDgegvdde3aFX1VwxlXPdvqJvdWPSWran2lI3Mz6eTPWMSlBPt+tLq\nXYNWSKzQ06WE+eVUmE61WDVw0x8+Jr5aubg8OA6DhdLI6IDqvFp7v4QNB0EvVPsu\nWCT6OgNC/wKBgAFfwZ8ArjnERtQc2Gji8GdUURpiAhNcch2NCx8NO/iDng44MZyt\nUCtwLYxV8az79vFNOKkxGS3FB9DopdGphKN4uwV7D23/YXfQQ9psSFYcVKdOrnug\n83lXeARaZPOYqATT/5g2ExXHJJyh3bWcctj+Jn6ggfD2E3A1VRsCia+lAoGACmUV\ndg5Rsfl8SA5Da6KTqNhUOUP25BMS3TDbrmzWDbw11thsH0onZUwZdmlg8WtWhgvz\n7nwy1mj6Z3FTcZeCFGTphi12Oexjl6/NsqM+/gSkA0S/nBZV6XN9tDimqsmoym6i\njCF3NCvEIIetg87tCTQQtBi0sO3WRorNvLmlPsUCgYAtSEFVqcTe6D6c6mNjyfhX\nrMJ2tR3l9q37C2k4GtXdx1LFeoNusEOyMU7GMTUL5gd7q571IW92mow5U04GmsXp\n2DfA41nVUT7sqnkVCoFt6LQDS+s/5v5KnxNZ23ZEul5Qbygfx9PQaZ/TuyaxZ6+S\nhJrcuKgiWaFyED4Lni/XsQ==\n-----END PRIVATE KEY-----\n",
        "client_email": "pythoncryptomessariaccount@crypto-messari.iam.gserviceaccount.com",
        "client_id": "112559430258363988070",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pythoncryptomessariaccount%40crypto-messari.iam.gserviceaccount.com"
    }
        
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '_fbp=fb.1.1723055733776.393052030482745864; __adroll_fpc=c56d747cb1638e03488a15b3f4abd0b4-1723591453615; drift_aid=e6590113-0bbc-4fe7-9564-d376a4b58f98; driftt_aid=e6590113-0bbc-4fe7-9564-d376a4b58f98; fpestid=uG-YaSUTRNYeF_dEznL5O6OeN_2UAVplc_pcMjSF6QcHVwCtSFHsJ1pEOhwYqO3hUo3HYg; _gid=GA1.2.1670702620.1723748944; _gat=1; gtm_session_start=1723748944159; _ga=GA1.1.1005670791.1723055732; drift_campaign_refresh=affb1c15-24c2-4c15-87e9-c635039996b9; __ar_v4=73HJZBAJDBHUPN4I7XOTD5%3A20240812%3A6%7CUUYIUUFVVRC3LHLHLA6FLF%3A20240812%3A6%7CNXMUJPTUJZGA3M5CXNKVV3%3A20240812%3A6; _ga_SZFYV030S1=GS1.1.1723748944.4.1.1723748960.44.0.1411122294',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }
    save = []
    
    # def __init__(self) -> None:
    #     self.session = requests.session()
    #     self.session.headers.update(self.headers)
    
    def get_listing(self):
        url = 'https://lakewoodranch.com/connect/events-list/'
        while True:
            try:
                response = requests.get(url,timeout=10)
                break
            except Exception as e:
                print(e)
        soup = BeautifulSoup(response.text,'html.parser')
        cards = soup.select('.row.event-line.fti.va-middle ')
        print('cards : ',len(cards))
        links = []
        for card in cards:
            a_link = card.a
            if a_link:
                links.append(a_link['href'])

        for item in links:
            while True:
                respon = self.get_data(url=item)
                if respon == 'connection':continue
                if respon == 'timeout':continue
                break

    def get_data(self,url:str):
        try:response = requests.get(url,timeout=10)
        except requests.exceptions.Timeout:return'timeout'
        except requests.exceptions.ConnectionError:return'connection'
        soup = BeautifulSoup(response.text,'html.parser')
        dic = {}
        addeventatc = soup.select_one('.addeventatc')
        if addeventatc == None:
            return None
        dic['title'] = addeventatc.select_one('.title').text.strip()
        dic['start'] = addeventatc.select_one('.start').text.strip()
        dic['end'] = addeventatc.select_one('.end').text.strip()
        dic['timeZone'] = addeventatc.select_one('.timezone').text.strip()
        dic['location'] = addeventatc.select_one('.location').text.strip()
        dic['description'] = addeventatc.select_one('.description').get_text('\n',strip=True)
        dic['event_link'] = url
        self.save.append(dic)
        print(dic['title'],len(self.save),sep=' | ')
    
    
    def open_sheet(self):
        df = pandas.DataFrame(self.save)
        df = df.replace(np.NAN,'')
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        gc = gspread.service_account_from_dict(self.creds)
     
        spreed_sheet_id = '1HIobsNi_E7xvmO3Fu0_DW7yHF4XExVZOTB7_oZ8E0Mg'
        sheet = gc.open_by_key(spreed_sheet_id)
        worksheet = sheet.worksheet('Sheet1')
        worksheet.batch_clear(["A1:EZ"])
        columns = df.columns.values.tolist()
        body = df.values.tolist()
        save = []
        save.append(columns)
        for item in body:
            #
            save.append(item)
        
        #pprint.pprint(save)
        worksheet.update(values=save, range_name='A1')
        print('exit - 0 finish | date: ',datetime.datetime.now() , ' | total: ' + str(len(self.save)))

        
if __name__ == '__main__':
    lakewood_class = lakewood()
    lakewood_class.get_listing()
    if lakewood_class.save != []:
        lakewood_class.open_sheet()
        
        
