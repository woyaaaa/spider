import requests

url = "https://fanyi.baidu.com/basetrans"

dataString = {"query": "魔镜魔镜告诉我",
        "from":"zh",
        "to": "en",
        "toke":"6cb026856ef193b19b0503d1d13cc921",
        "sign": "961969.675456"
        }

headers = {"User-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
            "Sec-fetch-mode": "cors",
            "Sec-fetch-site": "same-origin",
            "Origin": "https://fanyi.baidu.com",
            "Referer": "https://fanyi.baidu.com/",
            "Cookie":"BAIDUID=8DB9F82A77BA37DBDA29A1BF3C9193FE:FG=1; BIDUPSID=8DB9F82A77BA37DBDA29A1BF3C9193FE; PSTM=1572361749; pgv_pvi=3134441472; delPer=0; H_PS_PSSID=1443_21108_29568_29221_26350; PSINO=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1573875697; yjs_js_security_passport=0a79e41b42ec22ebc1be935825dde8edeed5e3dc_1573875697_js; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22slo%22%2C%22text%22%3A%22%u65AF%u6D1B%u6587%u5C3C%u4E9A%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; ZD_ENTRY=google; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1573875851; rsv_i=174ftbs1vpeG%2Fq7co%2BuE%2BpqZfB3KEe5znHKKy2%2FD3%2B2NoOMYY1ZYFEosFpmylkC4IWffpthM0NA2DrCT4fQMl8re7tAvYBI; FEED_SIDS=671435_1116_20; H_WISE_SIDS=130610_137150_137734_127759_114552_134724_136631_132548_135847_120169_137705_137380_137495_133995_136381_137979_132910_137690_131246_137750_132378_136681_118891_118867_118856_118831_118799_107311_136430_136094_133351_137900_136863_138324_138114_129650_136194_137104_133847_132552_138343_137467_134256_129644_131423_138199_137970_137465_136537_110085_135205_127969_138055_137912_137830_137252_138151_128195_136635_137208_137449; SE_LAUNCH=5%3A26231810_0%3A26231810; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1573909557; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1573909557"
            }

response = requests.post(url,data = dataString,headers = headers )

##print(response)
print(response.content.decode())