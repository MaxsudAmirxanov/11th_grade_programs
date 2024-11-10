# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import time

# # Настройка опций для браузера Chrome (без интерфейса)
# chrome_options = Options()
# chrome_options.add_argument("--headless")  # Убирает интерфейс браузера

# # Укажите путь к ChromeDriver
# driver_path = "/path/to/chromedriver"  # Замените на путь к вашему chromedriver

# # Создаем экземпляр браузера
# driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

# def search_bbc_news(keyword):
#     # Переходим на главную страницу BBC
#     driver.get("https://www.bbc.com/news")

#     # Ищем поле поиска и вводим ключевое слово
#     search_box = driver.find_element(By.CSS_SELECTOR, "input[id='orb-search-q']")
#     search_box.send_keys(keyword)
#     search_box.send_keys(Keys.RETURN)  # Нажимаем Enter для выполнения поиска

#     # Ждем загрузки результатов поиска
#     time.sleep(2)  # Ожидание, чтобы дать странице время загрузиться

#     # Парсим результаты поиска
#     headlines = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='promo-heading']")

#     # Выводим каждый заголовок и ссылку
#     if headlines:
#         print(f"Результаты поиска по запросу '{keyword}':\n")
#         for idx, headline in enumerate(headlines, 1):
#             print(f"{idx}. {headline.text.strip()}")
#             print(f"   Ссылка: {headline.get_attribute('href')}")
#     else:
#         print(f"По запросу '{keyword}' ничего не найдено.")

# # Ввод ключевого слова для поиска
# keyword = input("Введите ключевое слово для поиска на BBC: ")
# search_bbc_news(keyword)

# # Закрываем браузер
# driver.quit()


from selenium import webdriver  
from webdriver_manager.chrome import ChromedriverManager

# Using ChromedriverManager to automatically download and install Chromedriver  
driver = webdriver.Chrome(ChromedriverManager().install())

# Now you can use 'driver' to automate Chrome browser  
driver.get("https://www.example.com")

# Close the browser window  
driver.quit()  