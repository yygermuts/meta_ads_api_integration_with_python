from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adsinsights import AdsInsights


# 🔹 Substitua pelos seus dados
APP_ID = ''  # ID do App no Facebook Developers
APP_SECRET = ''  # Secret do App
ACCESS_TOKEN = ''  # Token gerado no Graph API Explorer
ACCOUNT_ID = ''  # Exemplo: act_1234567890

# 🔹 Inicializa a API do Facebook Ads
FacebookAdsApi.init(APP_ID, APP_SECRET, ACCESS_TOKEN)

# 🔹 Conectando à conta de anúncios
try:
    account = AdAccount(ACCOUNT_ID)
    campaigns = account.get_campaigns(fields=['id', 'name', 'status'])

    if campaigns:
        for campaign in campaigns:
            print(f"ID: {campaign['id']}, Nome: {campaign['name']}, Status: {campaign['status']}")
    else:
        print("Nenhuma campanha encontrada.")

except FacebookRequestError as e:
    print(f"❌ Erro ao acessar a API do Meta Ads: {e}")

    

# 🔹 Pegando métricas da conta
fields = [
    AdsInsights.Field.campaign_id,
    AdsInsights.Field.campaign_name,
    AdsInsights.Field.impressions,
    AdsInsights.Field.clicks,
    AdsInsights.Field.spend,
    AdsInsights.Field.conversions,
]

params = {
    'date_preset': 'last_7d',  # Últimos 7 dias
    'level': 'campaign',
}

insights = account.get_insights(fields=fields, params=params)

# 🔹 Exibindo os resultados
for insight in insights:
    print(f"Campanha: {insight['campaign_name']} | Impressões: {insight['impressions']} | Cliques: {insight['clicks']} | Gasto: {insight['spend']} | Conversões: {insight.get('conversions', 0)}")

