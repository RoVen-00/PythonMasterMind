from requests_html import HTMLSession, AsyncHTMLSession

graphic_card_url = "https://www.pccomponentes.com/msi-geforce-rtx-3060-ventus-2x-oc-lhr-12gb-gddr6"

session = HTMLSession()
r = session.get(graphic_card_url)

print(r)