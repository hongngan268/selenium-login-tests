from flask import Flask, render_template, request, redirect, url_for
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# Trang chủ với form đăng nhập
@app.route('/')
def home():
    return render_template('login.html')

# Đoạn mã xử lý khi người dùng submit form đăng nhập
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Sử dụng Selenium để kiểm thử đăng nhập
    driver = webdriver.Chrome()

    # Truy cập vào trang đăng nhập của Saucedemo
    driver.get("https://www.saucedemo.com/")
    
    # Tìm và điền thông tin đăng nhập
    username_field = driver.find_element_by_id("user-name")
    password_field = driver.find_element_by_id("password")
    login_button = driver.find_element_by_id("login-button")

    username_field.send_keys(username)  # Nhập tên đăng nhập từ form
    password_field.send_keys(password)  # Nhập mật khẩu từ form
    login_button.click()  # Nhấn nút đăng nhập

    time.sleep(2)  # Đợi một chút để trang tải
    
    # Kiểm tra kết quả đăng nhập
    if "inventory.html" in driver.current_url:
        driver.quit()
        return redirect(url_for('welcome'))
    else:
        driver.quit()
        return "Login Failed. Please try again."

# Trang đăng nhập thành công
@app.route('/welcome')
def welcome():
    return "Welcome to the application!"

# Chạy ứng dụng trên localhost
if __name__ == '__main__':
    app.run(debug=True)
