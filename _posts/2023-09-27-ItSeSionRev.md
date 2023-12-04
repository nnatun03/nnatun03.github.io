---
title: Write-Up IT SeSsion rev
date: 2023-09-27 4:55:00 +0700
categories: [CTF, FIA-FPTU, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
pin: true
---
# IT SeSsion rev
Hmm... A simple Calculator app definitely NOTHING special :))
## Tổng quan

- Để giải được bài này ta cần kiến thức về lỗi bảo mật SSTI (Server-Side Template Injection), cũng như syntax trong hệ điều hành Linux
- Công cụ: Burpsuite

## Phân tích bài

- Truy cập trang web, ta thấy được một ứng dụng máy tính tiền đơn giản, lúc này ta thử test qua một số chức năng của nó như cộng trừ nhân chia cơ bản thì phát hiện ra những điều như sau
    - Không thể sử dụng được phép chia `/`
    - Không thể sử dụng dấu cách ( `dấu +` )
- Mình đã thử encode nhưng có vẻ như bài vẫn filter được, nhưng tại sao 1 cái máy tính lại không thể sử dụng được phép chia và dấu + @@. Khó hiểu nhỉ, lúc này mình thử test 1 số payload về lỗi command injection nhưng có vẻ không hiệu quả.

<img src="/assets/writeup/cookie/IT SeSsion rev/0.png">
- Lúc này mình chuyển hướng qua khai thác lỗi khác, đó là SSTI (Server-Side Template Injection), giải thích sơ về SSTI như sau:
    - SSTI (Server-Side Template Injection) là một lỗ hổng bảo mật phổ biến xảy ra khi ứng dụng web không kiểm tra hoặc chống lại việc chèn mã template bên phía máy chủ (server-side templates) một cách an toàn. Điều này cho phép tin tặc chèn và thực thi mã bên phía máy chủ (thường là mã template) để tương tác với hệ thống hoặc ứng dụng web và có thể dẫn đến các hậu quả nghiêm trọng, bao gồm lấy thông tin nhạy cảm, thực hiện tấn công khác, hoặc kiểm soát máy chủ.
- Dấu hiệu nhận biết SSTI bao gồm:
    1. **Ký tự đặc biệt**: Kiểm tra sự xuất hiện của ký tự đặc biệt thường được sử dụng trong hệ thống template. Các ký tự như `{{`, **`{%`**, **`{#`**, **`$`**, **`|`**, `}}`, **`%}`**, **`#}`** có thể là dấu hiệu SSTI.
    2. **Sự kết hợp của ngôn ngữ template và mã bên phía máy chủ**: Khi thấy sự kết hợp của các lệnh hoặc cú pháp của ngôn ngữ template (như Jinja2, Twig, Freemarker) và biểu thức bên phía máy chủ, có thể là dấu hiệu SSTI.
    3. **Kết quả không mong muốn**: Khi thực hiện một số thao tác (như tính toán) và kết quả xuất hiện trên giao diện người dùng hoặc trong lỗi, đây có thể là dấu hiệu SSTI.
    4. **Đầu vào không được lọc**: Đầu vào người dùng không được kiểm tra hoặc lọc kỹ càng trước khi chèn vào template, dẫn đến khả năng chèn mã độc.
- Lúc này mình test thử payload sau

<img src="/assets/writeup/cookie/IT SeSsion rev/1.png">

- Ta nhận thấy server đã báo lỗi vì xuất hiện kí tự `{}` và phép toán của ta đã không được thực thi, tuy nhiến nếu ta chèn như thế này `{{ 1 x 3 }}` (thay x bằng * nhé vì mình dùng * push ko đc bị lỗi huhu)

<img src="/assets/writeup/cookie/IT SeSsion rev/2.png">

- Bạn có thể thấy rằng phép toán của ta đã được thực thi, và từ đây ta đã xác thực được rằng server có thể bị khai thác bằng lỗi SSTI
- Tuy nhiên lúc này ta phải kiểm tra xem thử template bài này là gì, ta sử dụng payload `{{ 7 x '7' }}` để test

<img src="/assets/writeup/cookie/IT SeSsion rev/3.png">

- Bạn có thể dễ dàng nhận thấy rằng kết quả của 7 x 7 không phải 49 mà là 1 chuỗi khác.
    - Khi bạn thực hiện `calc={{ 7 * '7'}}` trong một ngữ cảnh sử dụng một hệ thống template như Jinja2 hoặc một ngôn ngữ tương tự, dấu hai ngoặc mở `{{` và `}}` thường được sử dụng để định tuyến các biểu thức và lệnh.
    - Trong ví dụ trên, `7 * '7'` được giữa hai dấu ngoặc mở `{{` và `}}`, nhưng nó không được xem như một biểu thức số học bình thường trong ngữ cảnh của một hệ thống template. Thay vào đó, nó được xem như một chuỗi ký tự với một phép nhân giữa con số 7 và chuỗi '7'. Do đó, kết quả hiển thị là "7777777", trong đó số 7 được lặp lại bảy lần.

<img src="/assets/writeup/cookie/IT SeSsion rev/4.png">

                1 Số cách test với các template khác mình để cho bạn dễ hình dung ^^

- Okay, sau khi xác định được tempalte là Jinja2, mình thử test xem có thực thi được OS command không.

Payload: `{{self._TemplateReference__context.cycler.**init**.**globals**.os.popen('id').read()}}`

1. `self._TemplateReference__context`: Truy cập vào biến `context` của đối tượng `TemplateReference`. Thường được sử dụng để truy cập đối tượng chứa các dữ liệu template.
2. `cycler`: Đây có thể là một biến hay đối tượng có chứa thông tin về việc lặp lại hoặc chuyển đổi giữa các giá trị.
3. `__init__`: Gọi phương thức khởi tạo của đối tượng `cycler`.
4. `__globals__`: Truy cập vào namespace toàn cục của chương trình.
5. `os`: Truy cập vào module `os`, một module trong Python cung cấp các hàm để tương tác với hệ điều hành.
6. `popen('id').read()`: Sử dụng `os.popen` để thực thi lệnh `id` (hiển thị thông tin người dùng và nhóm hiện tại) trong hệ thống và đọc kết quả.

<img src="/assets/writeup/cookie/IT SeSsion rev/5.png">

- Việc bây giờ chúng ta cần làm là tìm flag trong hệ thống.
- Vì server như trước mình đã nói, server đã filter khoảng trắng ( dấu cách ), nên chúng ta phải bypass được filter đó, trong trường hợp này mình dùng `tab` , có chức năng xuống hàng và tác dụng của nó tương tự khoảng trắng.

payload:  `calc={{self._TemplateReference__context.cycler.**init**.**globals**.os.popen('ls<dấu TAB>-la').read()}}`

<img src="/assets/writeup/cookie/IT SeSsion rev/6.png">

- Bonus thêm là server cũng filter nốt chữ `cat` nên chúng ta sẽ dùng `head` và `tail` để đọc được nội dung của file, lúc này mình đọc Dockerfile và tìm được tập tin `/s3cret_fl4g_f1le.txt` lúc này ta bắt buộc phải tìm cách bypass được filter dấu `/`
    
<img src="/assets/writeup/cookie/IT SeSsion rev/7.png">
    
- các bạn có thể tham khảo hình dưới, nhưng bài này mình sẽ dùng hướng khác

<img src="/assets/writeup/cookie/IT SeSsion rev/8.png">

- Mình sẽ sử dụng lệnh `cd ..` để quay về thư mục gốc, kết hợp với `head*` để đọc toàn bộ tập tin

<img src="/assets/writeup/cookie/IT SeSsion rev/9.png">

- DONEEEE!
