# Baby Assert

## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về
- công cụ: Burpsuite

## Phân tích bài

- Truy cập trang web với giao diện như sau
    
    ![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled.png)
    
- Thử truy cập `/home`
    
    ![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%201.png)
    
- với parameter `/index.php?page=home` mình đã nghĩ ngay tới LFI, tuy nhiên sau khi test 1 lúc thì có vẻ như trang web không bị lỗi này. Tiếp tục kiểm tra các chức năng khác
- Ở `/About` thì không có gì tuy nhiên ở `/Secret` thì ta phát hiện rằng flag đã được thêm ngẫu nhiên các kí tự, điều đó làm mình suy luận rằng ta không thể đọc flag một cách thông thường vì mình không biết chính xác tên là gì —> bắt buộc phải RCE để tìm kiếm tên chính xác.
    
    ![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%202.png)
    
- Sau một lúc làm bài bế tắc thì mình quay lại phân tích đoạn code ở `/home`

```php
$file = "pages/" . $page . ".php";
assert(...$file...) or die("Detected hacking attempt!");
require_once $file;

```

- Biến `$file` ở đây là 1 untrusted data, bởi vì:
    - Nó được ghép từ biến `$page` mà không rõ giá trị của `$page` đến từ đâu. Có thể là do người dùng nhập vào, đọc từ request,...
    - Không có cách nào để kiểm tra trước xem giá trị của `$page` có hợp lệ hay đáng tin cậy không.
    - Ta có thể thiết lập `$page` là một giá trị nguy hiểm, ví dụ chứa ký tự ".." để thao túng đường dẫn file.
- Tuy nhiên ở đoạn code sau, biến `$file` lại được truyền vào function assert , từ đó mình tiếp tục kiểm tra xem có thể khai thác được gì khi untrusted data lọt vào function như assert không, việc mình làm là tìm hiểu assert là gì và những cách khai thác nó thì mình biết được rằng.
    - Không giống như các ngôn ngữ lập trình khác, PHP cho phép `assert()` có một khả năng đặc biệt, **nếu điều kiện kiểm tra được truyền vào dưới dạng chuỗi, `assert()` sẽ đánh giá nó như một đoạn mã PHP**.
    - Điều này có nghĩa nếu ta truyền vào một chuỗi cho `assert()`, nó sẽ hoạt động giống như hàm `eval()` và có thể thực thi các lệnh hệ thống.
    - Như vậy, lỗ hổng ở đây là việc có thể đưa mã độc vào `assert()` dưới dạng chuỗi, khiến nó thực thi mã độc đó và RCE
- Thử test lỗi LFI thông qua `assert()` với payload:
    
    `' and die(show_source('/etc/passwd')) or ‘`
    

---

![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%203.png)

- Tiếp đến RCE bằng hàm `system()` với payload:
    
    `' and die(system("whoami")) or '`
    

![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%204.png)

- Sau đó ls - la / và cuối cùng là cat tên flag thôi ^^
    
    ![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%205.png)
    

![Untitled](Baby%20Assert%2079b74a40af9641e8a1f13eb6f0f9940d/Untitled%206.png)