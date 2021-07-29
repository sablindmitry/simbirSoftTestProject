import gmail as gmail
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


#print('Enter your gmail address and password')
#gmail_id, password = map(str, input().split())

gmail_id = 'simbirsopttestwork@gmail.com'
password = 'Sdv9176283639'


try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://mail.google.com/")
    #driver.get(r"https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    driver.implicitly_wait(15)

    login_box = driver.find_element_by_xpath('//*[@id ="identifierId"]')
    login_box.send_keys(gmail_id)

    next_button = driver.find_element_by_xpath('//*[@id ="identifierNext"]')
    next_button.click()

    password_box = driver.find_element_by_xpath('//*[@id ="password"]/div[1]/div / div[1]/input')
    password_box.send_keys(password)

    next_button = driver.find_element_by_xpath('//*[@id ="passwordNext"]')
    next_button.click()
    driver.implicitly_wait(15)

    search_field = driver.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]')
    search_field.send_keys('Simbirsoft Тестовое задание')

    search_button = driver.find_element_by_xpath('//*[@id="aso_search_form_anchor"]/button[4]')
    search_button.click()
    print('login Successful')


    unread_email = driver.find_elements_by_class_name('zE')
    email_subject = driver.find_elements_by_class_name('bog')
    counter = 0
    for item in email_subject:
        if 'Simbirsoft Тестовое задание' == item.text:
            counter += 1
            print(item.text)
    print(f"Писем с искомой темой найдено {counter}")

except:
    print('Failed to login')

