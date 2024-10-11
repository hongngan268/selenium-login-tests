from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_login_success():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")  # Truy cập trang đăng nhập

    username = driver.find_element_by_id("user-name")  # Tìm trường nhập tên đăng nhập
    password = driver.find_element_by_id("password")  # Tìm trường nhập mật khẩu

    username.send_keys("standard_user")  # Nhập tên đăng nhập hợp lệ
    password.send_keys("secret_sauce")  # Nhập mật khẩu hợp lệ

    login_button = driver.find_element_by_id("login-button")  # Tìm nút đăng nhập
    login_button.click()  # Nhấn nút đăng nhập

    time.sleep(2)  # Đợi một chút để trang tải

    # Kiểm tra xem URL có chứa "inventory.html" để xác nhận đăng nhập thành công
    assert "inventory.html" in driver.current_url

    driver.quit()

def test_login_failure():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com/")  # Truy cập trang đăng nhập

    username = driver.find_element_by_id("user-name")  # Tìm trường nhập tên đăng nhập
    password = driver.find_element_by_id("password")  # Tìm trường nhập mật khẩu

    username.send_keys("wrong_user")  # Nhập tên đăng nhập không hợp lệ
    password.send_keys("secret_sauce")  # Nhập mật khẩu hợp lệ

    login_button = driver.find_element_by_id("login-button")  # Tìm nút đăng nhập
    login_button.click()  # Nhấn nút đăng nhập

    time.sleep(2)  # Đợi một chút để trang tải

    # Kiểm tra xem có thông báo lỗi hiển thị không
    error_message = driver.find_element_by_css_selector(".error-message-container").text
    assert "Username and password do not match" in error_message

    driver.quit()
