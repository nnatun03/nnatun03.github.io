# MR ROBOT

- Đầu tiên mình dùng nmap để scan tất cả các cổng đang mở

payload scan: `nmap -sC -sV -vv 10.10.45.82`

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled.png)

- Tiếp đến khi tuy cập vào bài, sau khi test qua 1 loạt chức năng thì có vẻ như đó chỉ là 1 trang HTML CSS xịn sò và hầu như không thể tác động gì vào server

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%201.png)

- Mình tiến hành scan những directory ẩn

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%202.png)

- Truy cập vào `/robots.txt` thì phát hiện key đầu tiên và fsocity.dic nhưng mình sẽ không dùng tới cái này

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%203.png)

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%204.png)

- Tiếp theo mình truy cập vào `/license` , kéo xuống dưới cùng và mình tìm được 1 đoạn mã base 64,  giải mã nó và mình được `elliot:ER28-0652` . Có vẻ như đây là 1 tên đăng nhập và mật khẩu

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%205.png)

- Tiếp tục tiến hành truy cập `/wp-login` và đăng nhập. có vẻ như ta sẽ được vào trang wordpress bình thường

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%206.png)

- Mình tiến hành tìm kiếm chỗ mà workpress sẽ tải lên nội dung vào server của trang web này

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%207.png)

- Mình sẽ chỉnh sửa nội dung của /404.php

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%208.png)

- Thử chèn thêm câu lệnh system(’ls -la /’);

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%209.png)

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2010.png)

- Sau khi test thành công, mình sẽ chèn thêm vào 1 đoạn reverse shell để thiết lập kết nối
    
    ![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2011.png)
    
- Bạn có thể tham khảo các loại reverse shell trên mạng, mình ko up được trên này vì bị detect mã độc :v

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2012.png)

- Mình đã tìm ra được flag thứ 2, tuy nhiên mình không thể đọc được

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2013.png)

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2014.png)

- Có vẻ như ta phải truy cập bằng robot thì mới đọc được, tuy nhiên file password mình vẫn có thể đọc

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2015.png)

- Sau khi giải mã MD5 là `abcdefghijklmnopqrstuvwxyz` thì mình thử truy cập vào robot để đăng nhập thì bắt buộc phải được chạy từ terminal

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2016.png)

- Mình dùng lệnh `python -c 'import pty; pty.spawn("/bin/sh")’`

Cụ thể:

- import pty: Nhập thư viện pty
- pty.spawn("/bin/sh"): Sử dụng hàm spawn() của pty để khởi chạy một phiên /bin/sh mới.
- /bin/sh: là đường dẫn tới shell interative trên Linux.
- pty.spawn sẽ tạo một pseudo-terminal (pty) mới và khởi chạy /bin/sh trên đó.

Như vậy, dòng lệnh Python trên sẽ mở một shell interative mới thông qua thư viện pty.

Điều này cho phép tương tác với shell đó thông qua stdin/stdout của chương trình Python hiện tại. Rất hữu ích trong việc đạt được shell access khi chỉ có quyền thực thi Python code.

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2017.png)

- Sau khi đăng nhập, mình tiến hành đọc flag thứ 2

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2018.png)

- Tiếp theo mình dùng `find / -perm -u=s -type f 2>/dev/null` để tìm tất cả các file thực thi SUID

Cụ thể:

- find /: tìm kiếm từ thư mục gốc /
- perm -u=s: tìm các file có quyền -rwsr-xr-x, tức có bit SUID được bật
- type f: chỉ tìm các file thông thường, loại trừ thư mục
- 2>/dev/null: chuyển hết các thông báo lỗi vào /dev/null để không hiển thị

Như vậy, lệnh trên sẽ tìm tất cả các file có quyền SUID trong hệ thống Linux và in ra đường dẫn của chúng mà không hiển thị thông báo lỗi.

Lệnh này thường được dùng để tìm các file SUID có thể dùng để leo thang đặc quyền (privilege escalation) trong quá trình kiểm tra bảo mật, pentest.

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2019.png)

- Mình phát hiện nmap đang được chạy dưới quyền ROOT, mình có thể tận dụng chế độ interactive của nmap để leo thang đặc quyền.
- dùng lệnh `nmap --interactive`  và `!sh`

Cụ thể:

- Trong chế độ interactive, người dùng có thể gõ các lệnh nmap một cách trực tiếp và xem kết quả ngay lập tức, thay vì phải chạy từng lệnh riêng lẻ.
- !sh trong chế độ interactive của nmap là một shortcut để chạy một shell.
- khi gõ !sh, nmap sẽ tạm thời thoát khỏi chế độ interactive và mở một shell trên hệ thống mà nmap đang chạy.
- Sau khi thoát khỏi shell (vd: gõ exit), bạn sẽ quay trở lại chế độ interactive của nmap.

Một số điểm cần lưu ý về !sh:

- Chỉ hoạt động nếu nmap được chạy với quyền sudo hoặc root.
- Cung cấp quyền truy cập shell với đặc quyền tương ứng với cách nmap được chạy.
- Cho phép thực thi nhanh các lệnh hệ thống như ls, ps, ifconfig... ngay trong nmap mà không cần phải mở thêm cửa sổ terminal.

![Untitled](MR%20ROBOT%20a8978d3f3b4c4dbcad30eecabfdeea91/Untitled%2020.png)

- done!