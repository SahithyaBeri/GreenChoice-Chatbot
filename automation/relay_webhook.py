import requests

RELAY_WEBHOOK = "https://hook.relay.app/api/v1/playbook/cmmlp48k40ht00qkocf5e3waf/trigger/IMXPFj4oLt0GRDtHp2bYTQ"

def send_to_relay(query, response):

    payload = {
        "query": query,
        "response": response
    }

    r = requests.post(RELAY_WEBHOOK, json=payload)

    return r.status_code