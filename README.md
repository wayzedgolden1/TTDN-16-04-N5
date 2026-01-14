<h2 align="center">
    <a href="https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin">
    🎓 Faculty of Information Technology (DaiNam University)
    </a>
</h2>
<div align="center">
    <p align="center">
        <img src="docs/aiotlab_logo.png" alt="AIoTLab Logo" width="170"/>
        <img src="docs/fitdnu_logo.png" alt="AIoTLab Logo" width="180"/>
        <img src="docs/dnu_logo.png" alt="DaiNam University Logo" width="200"/>
    </p>

[![AIoTLab](https://img.shields.io/badge/AIoTLab-green?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Faculty of Information Technology](https://img.shields.io/badge/Faculty%20of%20Information%20Technology-blue?style=for-the-badge)](https://dainam.edu.vn/vi/khoa-cong-nghe-thong-tin)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-orange?style=for-the-badge)](https://dainam.edu.vn)
</div>

## Công nghệ sử dụng

![Ubuntu](https://img.shields.io/badge/UBUNTU-orange?logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/GITLAB-black?logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/POSTGRES-blue?logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-v3.8+-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/security-grey)
![Bandit](https://img.shields.io/badge/bandit-yellow)


## 1. Cài đặt công cụ, môi trường và các thư viện cần thiết

### 1.1. Clone project.


<pre>
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
git checkout &lt;branch-name&gt;
</pre>

### 1.2. cài đặt các thư viện cần thiết
<p>Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết</p>

<pre>
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
</pre>

### 1.3. khởi tạo môi trường ảo.

<pre>
python3.10 -m venv ./venv
</pre>

<p>Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu</p>

<pre>
source venv/bin/activate
pip3 install -r requirements.txt
</pre>

## 2. Setup database

<p>Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.</p>

<pre>
docker-compose up -d
</pre>

## 3. Setup tham số chạy cho hệ thống

### 3.1. Khởi tạo odoo.conf

<p>Tạo tệp odoo.conf có nội dung như sau:</p>

<pre>
[options]
addons_path = addons
db_host = localhost
db_password = odoo
db_user = odoo
db_port = 5432
xmlrpc_port = 8069
</pre>

<p>Có thể kế thừa từ odoo.conf.template</p>

<p>Ngoài ra có thể thêm mổ số parameters như:</p>

<pre>
-c &lt;đường dẫn đến tệp odoo.conf&gt;
-u &lt;tên addons&gt; giúp cập nhật addons đó trước khi khởi chạy
-d &lt;tên database&gt; giúp chỉ rõ tên database được sử dụng
--dev=all giúp bật chế độ nhà phát triển
</pre>

## 4. Chạy hệ thống và cài đặt các ứng dụng cần thiết

<p>Người sử dụng truy cập theo đường dẫn http://localhost:8069/ để đăng nhập vào hệ thống.</p>

<p>Hoàn tất</p>
