import pytest
import requests

url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

user_agent_data = [{
        "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 "
        "(KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "expected_values": {"platform": "Mobile", "browser": "No", "device": "Android"}
    },
    {
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                      "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "expected_values": {"platform": "Mobile", "browser": "Chrome", "device": "iOS"}
    },
    {
        "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "expected_values": {"platform": "Web", "browser": "Chrome", "device": "Unknown"}
    },
    {"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
     "expected_values": {"platform": "Web", "browser": "Chrome", "device": "No"}
     },
    {"user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                   "Version/13.0.3 Mobile/15E148 Safari/604.1",
     "expected_values": {"platform": "Mobile", "browser": "No", "device": "iPhone"}
     }]


@pytest.mark.parametrize('data', user_agent_data)
def test_user_agent(data):
    user_agent = data["user_agent"]
    expected_values = data["expected_values"]
    response = requests.get(url, headers={"User-Agent": user_agent})
    resp_json = response.json()
    assert resp_json["platform"] == expected_values["platform"]
    assert resp_json["browser"] == expected_values["browser"]
    assert resp_json["device"] == expected_values["device"]
