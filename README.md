![Ubuntu](https://img.shields.io/badge/ubuntu-20.04-orange?logo=ubuntu&logoColor=white)
![GitLab](https://img.shields.io/badge/gitlab-repo-orange?logo=gitlab&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-db-blue?logo=postgresql&logoColor=white)

![Python](https://img.shields.io/badge/python-3.8+-blue?logo=python&logoColor=white)
![Bandit](https://img.shields.io/badge/security-bandit-yellow)


<p style="font-size:20px; font-weight:bold;"><b>1. Cài đặt công cụ, môi trường và các thư viện cần thiết</b></p>

<p><b>1.1. Clone project.</b></p>
<pre>
git clone https://gitlab.com/anhlta/odoo-fitdnu.git
git checkout &lt;branch-name&gt;
</pre>

<p><b>1.2. cài đặt các thư viện cần thiết</b></p>
<p>Người sử dụng thực thi các lệnh sau đề cài đặt các thư viện cần thiết</p>

<pre>
sudo apt-get install libxml2-dev libxslt-dev libldap2-dev libsasl2-dev libssl-dev python3.10-distutils python3.10-dev build-essential libssl-dev libffi-dev zlib1g-dev python3.10-venv libpq-dev
</pre>

<p><b>1.3. khởi tạo môi trường ảo.</b></p>

<pre>
python3.10 -m venv ./venv
</pre>

<p>Thay đổi trình thông dịch sang môi trường ảo và chạy requirements.txt để cài đặt tiếp các thư viện được yêu cầu</p>

<pre>
source venv/bin/activate
pip3 install -r requirements.txt
</pre>

<p><b>2. Setup database</b></p>

<p>Khởi tạo database trên docker bằng việc thực thi file dockercompose.yml.</p>

<pre>
docker-compose up -d
</pre>

<p><b>3. Setup tham số chạy cho hệ thống</b></p>

<p><b>3.1. Khởi tạo odoo.conf</b></p>

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

<p>-c &lt;đường dẫn đến tệp odoo.conf&gt;</p>
<p>-u &lt;tên addons&gt; giúp cập nhật addons đó trước khi khởi chạy</p>
<p>-d &lt;tên database&gt; giúp chỉ rõ tên database được sử dụng</p>
<p>--dev=all giúp bật chế độ nhà phát triển</p>

<p><b>4. Chạy hệ thống và cài đặt các ứng dụng cần thiết</b></p>

<p>Người sử dụng truy cập theo đường dẫn http://localhost:8069/ để đăng nhập vào hệ thống.</p>

<p>Hoàn tất</p>
