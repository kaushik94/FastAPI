curl -u kaushik@moneysave.io:zendesk https://moneysavehelp.zendesk.com/api/v2/triggers.json \
  -H "Content-Type: application/json" -X POST -d \
  '{
        "trigger": {
            "title": "Roger Wilco",
            "conditions": {
                "all": [
                    {
                        "field": "comment_is_public",
                        "value": "not_relevant" 
                    }
                ]},
            "actions": [{ "field": "notification_webhook", "value": "20455932" }],
            "category_id": "notifications"
        }
    }'