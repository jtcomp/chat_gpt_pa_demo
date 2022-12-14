import requests
import re  
import json

params = {
    "max_tokens" : 4097,

}

cookie = 'cf_clearance=LZXA9djBLCPAFWnovr0Q3P40ImP9t0Nn7RHQgCYvY70-1670987898-0-1-3e5340c5.f03eaa74.d109a37e-160; __Host-next-auth.csrf-token=481a4ce4b0386e19945bea7677857c568f4dda37fd25ef42d63146d4f96be693|9fdab85574ca641e1cb538fbd22ddba411c2674a5f97eababfe48869421b5478; __cf_bm=0m.IN9WUtudD5Pz_wfhmgdWyLNhpK.nF3DK6VbTFXmQ-1670987898-0-Aa47hBbBahoZlLDjOfe1btmuMPoDfjGg6JUoRhInrwJ9Jh0YDzcf1KGU8DwkCTmUiRlzILI1nS3DWbRHUSnGFQJQpPR6YluWR5gtDa3Sa4auuYtnKhUlYrZDkGzfXuWFRqkfyZJ1y+Q4oRkK0n5WbGrCsPvVX/ceeq2+6nrSo/732dbrSkw7N4pAfQItZsKKgw==; __Secure-next-auth.callback-url=https://chat.openai.com/; mp_d7d7628de9d5e6160010b84db960a7ee_mixpanel={"distinct_id": "user-nu0WqZl4h2PW1Ne4pTpWoJ4w","$device_id": "1850ea40198d1a-0b4ae1ae2112fd-17525635-13c680-1850ea40199d80","$search_engine": "google","$initial_referrer": "https://accounts.google.com/","$initial_referring_domain": "accounts.google.com","$user_id": "user-nu0WqZl4h2PW1Ne4pTpWoJ4w"}; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..X3V-GifOKykPD_CI.J9o-gDAUb5RnTE_gmNqm9sxH3GTyF1rbTTh17HGamar7jsNhfPEX9pHbgBYSHXmRMPPINpvuVQficByq76BIJYCITzdwL8mlCdbq-sFJ5VX75sq75dfThS8knG9JQF-4r_fpbflX9seS5IRP6JHGtwghwi79jp_WWmYgop1lXe8uh5zoZ9UYTf_pKAIIMUT0MW-Oe1wwjN_rNjIoZh1rKGCTpeIzPKMi2HgrAK5B_iS8i17yd3K9rwZoe7KeDqfihCRJmqIGiIbcy-0tDpl_aY5D6EZAQoDCw-b4PoRaedTSaaxkA86g8PrvmSgifYETPe4kVHvWteXtKdYWbW0Rq4yfBJmmPmUvNhCtiDJCZf6HghLi3_vneTNR9gp4Y8bbWxuJmxT6PhF1Tjtj_N8BKiN_n6kvlzt_sDoy6xl4YShNFDwRD-P7oxqwA-PZFj2I7aCBnWW6G37SO6iIdJP2WBZuvVBh1lT6BeKGn3poASNoJyiQNTlItnhxZduKZInSMKme0X7InZ4dnP3IFrenSwLkZZDuW1Dn-K-bEFDDP52-pDt7n7Xztdk7nVoipZ30e0CmOD2nO85wTwOfjyi9HH1mCPAdPNcJG80PZdSxZdvijvBmXysdKiD29NpXWZvinskohCkOjQupvZvaCLoe5sk5I-yX9jEs-qGG98XdBUvm7iIYhnaKieSdQal8rL8K3pqvGtWFaehuiXtMjVhsQFqVotd0YiW-QFrdrtdA8Id9o5DzU5MfC81MPdtyF6OoYmG3BIq1xExNoeZiG0oWVpSlyW9qvYbX5OpSJZmtb4Ypx3XB9pTl-CoMI2VLdrkWThxudXFT7CNM2qL-HMUUz4_-hTWSkY2L1N-YFxmCX7jwMHi0_HWb9mY9fu4g9d_8Ch-wvCrHhUS86Qo5KqbzYQ3e2J3DLdkwDmsN6zIBim1RGy9c8lFpmp15OeUb2O66avSoFoVyMfYwJN3WGVZw847oXwlWAn_vg4vVIgZym73ddIdKpXQJVRKmQda0XLINV6WP5L2BQOZ9voaLEEQ-lnGe_3lnlFDD4mnDyp8k-eNvT07oaOUrniFb-V3nhf2OJtw-mMg07MVGd10TzRjF7CbDFeoWRQQh3N3Am80gCMu9njSFyww_w-Pvg_J73-D2c8bkH0euhC1jfIRVuNYbJKvUlJY5tEFg140fr-LS3r0S70H3Ix0TouZMIEl10VAcNzhJNabOSXL-UrYz415tz482azeIYPQKRFKfmNLXJVqPI-6UZbmHPRTYIsLsCkl3cdq2j1wXiN4cI5g4k9lrvGf2Q_fifWwYDS1SkFiJrWqTnL-MuW5CsEVtJwhJShhtuLJFSG-b3Xo3lzLH5E6TuIi87zTGva1HJVaGjgW4VzdLHqHBafj0ZhnQ_erWzgN-MumDiQyc0ck3uMEitUm6n52A92zGxgczD9xH6J8ur1wtcVbAQ3_AGDmPeOp_buk4SF8Sk7CzqLgF9rTZReczk8A8LlcAJq-rfm564nbld_4Z2kF9hm1bIi76ENAb3w6js6i6tkGO3RP215emz5zwhAKxhNxd7X8Hp-CeTFsji2TuuU8OStZlmYE99H-GXIxCnOvm1BFkF1G7e_FuKtwluSp4x3ngK2I_dlc4nsg4GNl3eJom3HubWkmJ5ntcIMUqgMCbshkCNIV27IKkq0_xwgNTHAxe_ZJkqC4YVJr0TKFUekZ5POq1LwhMfhY3V1U5ot1EkWZYM8Azw0Vz4rqZ2v8EtOwwDaZs2Y7BPDHNg9p_oTBH7uiYUeBs6NsDoFfktwKNL1BxcDSkyDwEcHhR1_2hR8W8e_xBaVKKdSGaYqarLOnplAzvq7q2mjhTKEAu5a37HoHLaEGPJltZ5mNt7x_jTatkuuBXEVZejQxYEBXLPDeFrerc_qqnrOk3ibydXGN7KjxcmXGUz6pw8LDec6LbhVk_exTpCIsYnGj1QANKVmRCZD1v3mZ3Pr-CXpRZHVrGs8D8H4vYsuWdNin9UNdKfDC63g-dmavKn3WTLU6bbUHpFrOy6rZJxXKYw1erkLJaVDVE7xVn4drP0rkm5bGnhCb9xXtQsD4jFqmg3JzRIULoqC0ryLm7GL8tF-DCyG6sHRSfkAh5BWWO2ryyh8FzxbYc9D4W-QbYREH7XnpE-zGapaF4XGDThZA5A5-vQpGv31B9g0kbWaBEj8c924lj0oJpnyJk7BYZhhOMuYnws7NONSkU0EEJmBOSJjhuyQo9cmOfH2tMiykJMQ.TEqVZsefeU2OeyzYSkxN5w'

def parseResponse(gpt_out_string):
    array = json.loads(gpt_out_string)["message"]["content"]["parts"]
    return array[0] if len(array) == 1 else ""

# TODO add conversion id i get back from open AI so it has context
def gpt_resp_iter(new_tokens):
    # try: 
        with requests.post('https://chat.openai.com/backend-api/conversation',
                        json={
                            "action": "next",
                            "messages": [
                                {
                                    "id": "6e06a36d-c6f1-4e89-955e-49817d3fc6c9", # ??
                                    "role": "user",
                                    "content": {
                                        "content_type": "text",
                                        "parts": [new_tokens]
                                    }
                                }
                            ],
                            "parent_message_id": "81cd839f-e640-48a1-b9b2-3c817d76bd34", # should figure out what this does
                            "model": "text-davinci-002-render"
                        },
                        headers={
                            "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik1UaEVOVUpHTkVNMVFURTRNMEZCTWpkQ05UZzVNRFUxUlRVd1FVSkRNRU13UmtGRVFrRXpSZyJ9.eyJodHRwczovL2FwaS5vcGVuYWkuY29tL3Byb2ZpbGUiOnsiZW1haWwiOiJqb2huQGxldHNiZWxlZ2VuZHMuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdlb2lwX2NvdW50cnkiOiJVUyJ9LCJodHRwczovL2FwaS5vcGVuYWkuY29tL2F1dGgiOnsidXNlcl9pZCI6InVzZXItbnUwV3FabDRoMlBXMU5lNHBUcFdvSjR3In0sImlzcyI6Imh0dHBzOi8vYXV0aDAub3BlbmFpLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTYwMDcwMTY0OTcyNDYyNzIzOCIsImF1ZCI6WyJodHRwczovL2FwaS5vcGVuYWkuY29tL3YxIiwiaHR0cHM6Ly9vcGVuYWkuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTY3MDk2NDYxNSwiZXhwIjoxNjcxMDA3ODE1LCJhenAiOiJUZEpJY2JlMTZXb1RIdE45NW55eXdoNUU0eU9vNkl0RyIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwgbW9kZWwucmVhZCBtb2RlbC5yZXF1ZXN0IG9yZ2FuaXphdGlvbi5yZWFkIG9mZmxpbmVfYWNjZXNzIn0.oqwHZVdVflixnbPUdeY7QBHgIHbLuQRtJwixPgsRKBD8jW5ti1WNqj2J4t-HzIl2zKzfLxEOrlENBMlbmO-fbaEtoJkg_I_L3UoeVY1WiDpgYBCgJTQJugb0cc1VkHPFWamvxOU0gPhqSVuS6HO0AqjKgOWkWMekxfxLEoINkm-5lc-aLGjk_rNOY791DUMaxt2REwn_S6vCQk8rFlwiw5Dxp-f_QZ2-6d3vyLUbCDUTOgwhRkdx0sqzwjVkDs_IMYgyM_ABy3sq4f3769pinJP7FVOxtFalqMLOcnCylD6NowpvPJrBpY9VL5UUNWcyZyBp2z2j2ZuJ9whSqUpHdQ",
                            "Cookie": cookie,
                            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
                        }, stream=True) as resp:
            current = ""
            for line in resp.iter_lines():
                string = line.decode("utf-8").strip().replace("data: ", "")
                if string != "" and string != "[DONE]":
                    next = parseResponse(string)
                    yield next[len(current):] 
                    current = next
            resp.close()
