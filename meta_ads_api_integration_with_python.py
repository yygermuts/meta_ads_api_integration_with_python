from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.exceptions import FacebookRequestError
from facebook_business.adobjects.adsinsights import AdsInsights


# 🔹 Substitua pelos seus dados
APP_ID = '629584753153266'  # ID do App no Facebook Developers
APP_SECRET = '54873acbafd03ce1d8f2a50634940409'  # Secret do App
ACCESS_TOKEN = 'EAAI8mpZBRVPIBOwfKyK3GHusJ2v9Q7WcJ4lhZBqz80ZAqN4osdlyokbDZBw9vgWCkC9ctnlj1Ot9UpzQcxYq6CEbhiah6BhtU99fnJkKqOihJ2VMyFgw1PVQJ9xRYL4Jt2CItfZCE8E72fdmRBUCeAWSmuqxXUJlrodZAZBzeZByPViHUEN21ThtZCZB8jymeNWjnu'  # Token gerado no Graph API Explorer
ACCOUNT_ID = 'act_103272870037078'  # Exemplo: act_1234567890

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

