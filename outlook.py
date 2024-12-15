import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Fungsi untuk membuat username dan password acak
def generate_random_string(length=8):
    """Generate a random string of uppercase, lowercase letters and digits."""
    import random
    import string
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))

# Fungsi untuk mengisi form pendaftaran akun Outlook
def create_outlook_account():
    # Set up Selenium WebDriver
    chrome_options = Options()
    
    # Tentukan lokasi binary Chrome secara eksplisit
    chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # Sesuaikan dengan path di sistem kamu
    
    chrome_options.add_argument("--headless")  # Menjalankan di background tanpa membuka browser
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Akses halaman pendaftaran Outlook
        driver.get('https://signup.live.com/')

        # Tunggu halaman sepenuhnya dimuat
        import time
        time.sleep(2)

        # Isi form dengan data acak
        username = generate_random_string(10) + "@outlook.com"
        password = generate_random_string(12)

        # Temukan dan isi elemen formulir
        driver.find_element(By.NAME, 'loginfmt').send_keys(username + Keys.RETURN)
        time.sleep(2)

        # Klik tombol "Next"
        driver.find_element(By.ID, 'idSIButton9').click()
        time.sleep(2)

        # Masukkan password
        driver.find_element(By.NAME, 'passwd').send_keys(password)
        time.sleep(2)

        # Klik tombol "Sign in"
        driver.find_element(By.ID, 'idSIButton9').click()
        time.sleep(2)

        # Klik tombol "Yes" jika ditanya apakah ingin menyimpan informasi login
        try:
            driver.find_element(By.ID, 'idSIButton9').click()
            time.sleep(2)
        except:
            pass  # Jika tombol tidak ada, lanjutkan

        # Tunggu hingga akun berhasil dibuat (misalnya verifikasi email atau langkah verifikasi lainnya)
        print(f"Account created with username: {username} and password: {password}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Menutup browser setelah selesai
        driver.quit()

if __name__ == '__main__':
    # Membuat 5 akun Outlook secara acak
    for _ in range(5):  # Ganti 5 dengan jumlah akun yang ingin dibuat
        create_outlook_account()
        time.sleep(5)  # Jeda antar pembuatan akun (untuk menghindari deteksi otomatisasi)
