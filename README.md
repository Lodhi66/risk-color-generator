# risk-color-generator

This microservice is fully functioning and takes a POST request, which contains a JSON like this:
`{"risk": 45}`

The response will contain the risk number and a color corresponding to the risk number. Numbers
may be ints or floats and can be between 0 and 100.

## Request data using Flask (example code)

```
import requests

def send_request(risk):
    url = "http://127.0.0.1:5000/risk-color"
    payload = {"risk": risk}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return data["color"]
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the server: {e}")
        return None
```

# Response example (JSON)

`{"risk": risk_percentage, "color": color}`

# Sequence diagram

