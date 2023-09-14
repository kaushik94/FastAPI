$response = curl -X POST https://moneysavehelp.zendesk.com/api/v2/webhooks \
  -u kaushik@moneysave.io:zendesk \
  -H "Content-Type:application/json" \
  -d '{
    "webhook": {
      "name": "TEST_WEBHOOK_CREATION_VIA_FASTAPI",
      "status": "active",
      "endpoint": "https://fastapi-production-16e7.up.railway.app/webhook",
      "http_method": "POST",
      "request_format": "json",
      "subscriptions": [
        "conditional_ticket_events"
      ]
    }
  }'

echo $response.webhook.id
