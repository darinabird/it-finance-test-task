from urllib.parse import urlparse, parse_qs

url = "https://google.ru/?wmid=242&clickid=92c84d0f8c034531ace41792bd8bcc05&Mookid=zoSIq0bZhDXE"

# Разбиваем URL на его составные части
parsed_url = urlparse(url)

# Получаем словарь параметров запроса из URL
query_params = parse_qs(parsed_url.query)

# Получаем значение параметра "clickid"
clickid_value = query_params.get('clickid')
if clickid_value:
    clickid_value = clickid_value[0]

print(clickid_value)