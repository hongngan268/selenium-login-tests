import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Khởi tạo Edge WebDriver
service = Service(EdgeChromiumDriverManager().install())
options = Options()
options.headless = True  # Để trình duyệt hiển thị
driver = webdriver.Edge(service=service, options=options)

# Hàm mở trang đăng ký
def open_signup_page():
    print("Mở trang đăng ký...")
    driver.get("file:///C:/Users/vuhon/selenium-login-tests/signup.html")  # Đường dẫn tới file signup.html

# Hàm định nghĩa lại các trường dữ liệu
def define_fields():
    username_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "username")))
    password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "password")))
    confirm_password_field = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "confirm-password")))
    signup_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "signup-button")))
    return username_field, password_field, confirm_password_field, signup_button

#----------------------------------------------------------------------------------------------------
# Test case 1: Đăng ký thành công với thông tin hợp lệ
def test_successful_signup():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra đăng ký thành công với thông tin hợp lệ...")
    username_field.send_keys("validUser1")  # Username hợp lệ
    password_field.send_keys("validPassword")  # Password hợp lệ
    confirm_password_field.send_keys("validPassword")  # Xác nhận Password hợp lệ
    time.sleep(1)
    signup_button.click()

    time.sleep(2)  # Đợi một chút để xem kết quả

    # Kiểm tra trang chào mừng
    try:
        assert "Welcome" in driver.page_source
        print("Test 1 Passed: Đăng ký thành công.")
    except Exception as e:
        print(f"Test 1 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 2: Không đúng định dạng của username - Chỉ có số
def test_invalid_username_format():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra không đúng định dạng của username...")
    username_field.send_keys("12345")  # Không có chữ cái đầu tiên
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("validPassword")
    time.sleep(2)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho username không hợp lệ
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Tên đăng nhập không hợp lệ. (Phải bắt đầu bằng chữ cái, ít nhất 5 ký tự, chỉ chứa chữ và số)" in error_message.text or "Tên đăng nhập không đúng định dạng." in error_message.text
        print("Test 2 Passed: Không đúng định dạng của username - Chỉ có số")
    except Exception as e:
        print(f"Test 2 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 3: Không đúng định dạng của username – Chỉ có chữ
def test_username_only_letters():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra username chỉ có chữ...")
    username_field.send_keys("abcdef")  # Chỉ có chữ
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("validPassword")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho username không hợp lệ
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Tên đăng nhập không hợp lệ. (Phải bắt đầu bằng chữ cái, ít nhất 5 ký tự, chỉ chứa chữ và số)" in error_message.text
        print("Test 3 Passed: Không đúng định dạng của username – Chỉ có chữ")
    except Exception as e:
        print(f"Test 3 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 4: Không đúng định dạng của username – có kí tự đặc biệt
def test_username_special_characters():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra username có ký tự đặc biệt...")
    username_field.send_keys("user@name1!")  # Username có ký tự đặc biệt
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("validPassword")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho username không hợp lệ
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Tên đăng nhập không hợp lệ. (Phải bắt đầu bằng chữ cái, ít nhất 5 ký tự, chỉ chứa chữ và số)" in error_message.text
        print("Test 4 Passed: Không đúng định dạng của username – có kí tự đặc biệt")
    except Exception as e:
        print(f"Test 4 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 5: Không đúng định dạng của username – không đủ 5 ký tự
def test_username_unenough():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra username có ký tự đặc biệt...")
    username_field.send_keys("user!") 
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("validPassword")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho username không hợp lệ
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Tên đăng nhập không hợp lệ. (Phải bắt đầu bằng chữ cái, ít nhất 5 ký tự, chỉ chứa chữ và số)" in error_message.text
        print("Test 5 Passed: Không đúng định dạng của username – không đủ 5 ký tự")
    except Exception as e:
        print(f"Test 5 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 6: Bỏ trống username
def test_empty_username():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra bỏ trống username...")
    username_field.send_keys("")  # Username trống
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("validPassword")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho username trống
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Bỏ trống tên đăng nhập." in error_message.text
        print("Test 6 Passed: Bỏ trống username.")
    except Exception as e:
        print(f"Test 6 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 7: Không đủ ký tự của password
def test_invalid_password_length():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra không đủ ký tự của password...")
    username_field.send_keys("validUser3")
    password_field.send_keys("123")  # Password ngắn
    confirm_password_field.send_keys("123")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho password không đủ ký tự
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Mật khẩu phải có ít nhất 8 ký tự." in error_message.text
        print("Test 7 Passed: Không đủ ký tự của password.")
    except Exception as e:
        print(f"Test 7 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 8: Bỏ trống password
def test_empty_password():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra bỏ trống password...")
    username_field.send_keys("validUser6")
    password_field.send_keys("")  # Password trống
    confirm_password_field.send_keys("")
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho password trống
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Bỏ trống mật khẩu." in error_message.text
        print("Test 8 Passed: Bỏ trống password.")
    except Exception as e:
        print(f"Test 8 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 9: Confirm password không giống với password
def test_mismatched_passwords():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra confirm password không giống với password...")
    username_field.send_keys("validUser4")
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("differentPassword")  # Password không khớp
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho password không khớp
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Xác nhận mật khẩu không khớp." in error_message.text
        print("Test 9 Passed: Confirm password không giống với password.")
    except Exception as e:
        print(f"Test 9 Failed: {e}")

#----------------------------------------------------------------------------------------------------
# Test case 10: Bỏ trống confirm password
def test_empty_confirm_password():
    open_signup_page()
    username_field, password_field, confirm_password_field, signup_button = define_fields()

    print("Đang kiểm tra bỏ trống confirm password...")
    username_field.send_keys("validUser7")
    password_field.send_keys("validPassword")
    confirm_password_field.send_keys("")  # Confirm Password trống
    time.sleep(1)
    signup_button.click()

    time.sleep(2)

    # Kiểm tra thông báo lỗi cho confirm password trống
    try:
        error_message = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, "message")))
        assert "Bỏ trống xác nhận mật khẩu." in error_message.text
        print("Test 10 Passed: Bỏ trống confirm password.")
    except Exception as e:
        print(f"Test 10 Failed: {e}")



# Gọi các hàm kiểm thử
test_successful_signup()
test_invalid_username_format()
test_username_only_letters()
test_username_special_characters()
test_username_unenough()
test_empty_username()
test_invalid_password_length()
test_empty_password()
test_mismatched_passwords()
test_empty_confirm_password()


# Đóng trình duyệt
print("Đang đóng trình duyệt...")
driver.quit()
