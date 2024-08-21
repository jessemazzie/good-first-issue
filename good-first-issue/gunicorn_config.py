workers = 2
threads = 4
bind = "0.0.0.0:8000"
forward_allow_ips = "*"
secure_scheme_headers = {"X-Forwarded-Proto": "https"}
