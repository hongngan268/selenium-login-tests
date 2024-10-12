import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.microsoft import EdgeChromiumDriverManager


from webdriver_manager.chrome import ChromeDriverManager

# Khởi tạo Chrome WebDriver với WebDriver Manager
service = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--headless')  # Chạy không có giao diện đồ họa
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Khởi tạo Chrome WebDriver
driver = webdriver.Chrome(service=service, options=options)


# Khởi tạo Edge WebDriver với WebDriver Manager
# service = Service(EdgeChromiumDriverManager().install())

# options = Options()
# options.headless = True  # Chạy trình duyệt trong chế độ headless
# options.add_argument('--no-sandbox')  # Bỏ qua sandbox
# options.add_argument('--disable-dev-shm-usage')  # Giảm sử dụng bộ nhớ chia sẻ


# Cài đặt và sử dụng EdgeDriver
# service = Service()  # Cung cấp đường dẫn nếu cần
# options = Options()
# options.headless = False  # Để trình duyệt hiển thị, dễ quan sát quá trình kiểm thử

# Khởi tạo Edge WebDriver
driver = webdriver.Edge(service=service, options=options)

# Mở trang login của Sauce Demo
print("Mở trang login của Sauce Demo...")
driver.get("https://www.saucedemo.com/")

# Đợi trang đăng nhập tải xong và kiểm tra tiêu đề
try:
    WebDriverWait(driver, 30).until(EC.title_contains("Swag Labs"))
    print("Tiêu đề trang đã kiểm tra thành công.")
except Exception as e:
    print(f"Lỗi khi kiểm tra tiêu đề: {e}")

# --------------------------------------------------------------
# Test 1: Đăng nhập thành công với username và password hợp lệ
print("Đang kiểm tra đăng nhập thành công với thông tin hợp lệ...")
try:
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "inventory_container")))
    print("Test 1 Passed: Đăng nhập hợp lệ.")
except Exception as e:
    print(f"Test 1 Failed: {e}")

# Đăng xuất trước khi test case 2
try:
    menu_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "react-burger-menu-btn")))
    menu_button.click()
    logout_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    logout_button.click()
    print("Đã đăng xuất thành công.")
except Exception as e:
    print(f"Lỗi khi đăng xuất: {e}")

# --------------------------------------------------------------
# Test 2: Đăng nhập không hợp lệ với username và password sai
print("Đang kiểm tra đăng nhập không hợp lệ với username và password sai...")
try:
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    username_field.clear()
    password_field.clear()
    username_field.send_keys("wrong_user")
    password_field.send_keys("wrong_password")
    login_button.click()

    error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container")))
    assert "Epic sadface" in error_message.text
    print("Test 2 Passed: Đăng nhập không hợp lệ.")
except Exception as e:
    print(f"Test 2 Failed: {e}")

# --------------------------------------------------------------
# Refresh lại trang sau Test 2
driver.refresh()

# Test 3: Đăng nhập với username trống
print("Đang kiểm tra đăng nhập với username trống...")
try:

    # Tìm lại element sau khi trang refresh
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    # Clear các trường dữ liệu trước khi test
    username_field.clear()
    password_field.clear()

    # Username trống
    username_field.send_keys("")  
    password_field.send_keys("secret_sauce")
    login_button.click()

    time.sleep(5)
    assert "Epic sadface" in driver.page_source
    print("Test 3 Passed: Username trống.")
except AssertionError:
    print("Test 3 Failed: Không có lỗi khi username trống.")


# --------------------------------------------------------------
# Refresh lại trang sau Test 3
driver.refresh()

# Test 4: Đăng nhập với password trống
print("Đang kiểm tra đăng nhập với password trống...")
try:
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    username_field.clear()
    password_field.clear()
    username_field.send_keys("standard_user")
    password_field.send_keys("")  # Không điền password
    login_button.click()

    time.sleep(5)
    assert "Epic sadface" in driver.page_source
    print("Test 4 Passed: Password trống.")
except AssertionError:
    print("Test 4 Failed: Không có lỗi khi password trống.")

# --------------------------------------------------------------
# Refresh lại trang sau Test 4
driver.refresh()

# Test 5: Đăng nhập với cả username và password trống
print("Đang kiểm tra đăng nhập với cả username và password trống...")
try:
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    username_field.clear()
    password_field.clear()
    username_field.send_keys("")  # Không điền username
    password_field.send_keys("")  # Không điền password
    login_button.click()

    time.sleep(5)
    assert "Epic sadface" in driver.page_source
    print("Test 5 Passed: Cả 2 trường trống.")
except AssertionError:
    print("Test 5 Failed: Không có lỗi khi cả 2 trường trống.")

# --------------------------------------------------------------
# Refresh lại trang sau Test 5
driver.refresh()

# Test 6: Đăng nhập với user bị khóa
print("Đang kiểm tra đăng nhập với user bị khóa...")
try:
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "user-name")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "login-button")))

    username_field.clear()
    password_field.clear()
    username_field.send_keys("locked_out_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    time.sleep(5)
    assert "Epic sadface" in driver.page_source
    print("Test 6 Passed: User bị khóa.")
except AssertionError:
    print("Test 6 Failed: Không có lỗi khi user bị khóa.")


# --------------------------------------------------------------
# Đóng trình duyệt
print("Đang đóng trình duyệt...")
driver.quit()
