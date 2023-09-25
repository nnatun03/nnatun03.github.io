---
title: Write-Up MAGIC login
date: 2023-09-17 12:34:01 +0700
categories: [CTF, Cookie Hân Hoan, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
Hãy quan sát chức năng đăng nhập, nó có tồn tại những lỗ hổng nghiêm trọng. FLAG được lưu trong /flag.txt hãy tìm cách đọc được chúng.

## **Tổng quan**

- Để giải được challenge này, ta cần vận dụng kiến thức về Loose Comparison và File upload Vulnerability.
- Đối với PHP, Loose Comparison được thể hiện qua biểu tượng ‘==’, hiểu nôm na có nghĩa là so sánh hai giá trị mà không cần quan tâm đến Data types. Cụ thể hơn khi chạy câu lệnh echo 0 == '0' thì kết quả sẽ trả về 1(tương đương với True), còn trong trường hợp khác nếu viết là echo 1 == '0' thì sẽ không hiển thị giá trị 1 như câu lệnh trước (đồng nghĩa với False).
- công cụ: Burpsuite

## Phân tích bài
- vào bài thì đập vào mặt là 1 cái form login, đương nhiên việc đầu tiên là phải view-source xem bú liếm đc gì ko, quả nhiên được đoạn code =)) đọc thì thấy chắc đây là cơ chế login của bài này.

<img src="/assets/writeup/cookie/MAGIC LOGIN/0.png">

- Dễ dàng nhận định ngay rằng không thể tận dụng SQLi được rồi. Đoạn code này cũng không hẳn là quá phức tạp, nếu password nhập vào `($pas)` qua được bước check `$pas == “0”` thì ta sẽ bypass được bước login và được điều hướng tới trang upload. Như bình thường thì cứ nhập 0 vào là được thôi, nhưng như vậy thì lại thành ra quá dễ dàng rồi.
- Khúc lắt léo nằm ở dòng code:

`$pas = hash(‘sha256’,mysql_real_escape_string($_POST[‘password’]));`

Sau khi được filter qua hàm để chống SQLi, password sẽ được đưa vào hàm băm SHA256, và hiển nhiên là không có trường hợp nào sha256 trả về một giá trị bằng 0 cả.

- Đến đây có một kiến thức nữa ta cần biết, đó là 0e, đối với PHP, có nghĩa là 0 mũ,ví dụ như 0e3 chính là cách viết của 0 mũ 3. Ta cũng nhận thấy rằng bước check password sử dụng dấu `‘==’`, dấu hiệu của **Loose Comparison.**
- Kết hợp những dữ kiện này lại, việc cần làm giờ đây chính là nhập một giá trị nào đó cho password sao cho sau khi password được đưa vào hàm băm sha256 ta sẽ được một chuỗi 0e…(0 mũ mấy vẫn cứ là 0 thôi mà ^^).
- Và giá trị này là gì thì google trong phút mốt là ra: 34250003024812.

<img src="/assets/writeup/cookie/MAGIC LOGIN/1.png">

- nhập đại tên gì cũng được, vì coder lỏ quá nên chỉ cần nhập đúng pass là chuỗi vừa search được là sẽ bypass thành công :D

<img src="/assets/writeup/cookie/MAGIC LOGIN/2.png">

- • tới đây thì phải vận dụng kiến thức File upload, nhưng vẫn tiếp tục view-source để xem có gì không.

<img src="/assets/writeup/cookie/MAGIC LOGIN/3.png">

- đọc mã nguồn thì thấy không hạn chế gì lắm, up thẳng shell lên luôn :D

payload shell: `system(“cat /flag.txt”)`

<img src="/assets/writeup/cookie/MAGIC LOGIN/4.png">
