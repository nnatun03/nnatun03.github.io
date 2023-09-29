---
title: Bypass SAFE EXAM
date: 2023-09-29 4:55:00 +0700
categories: [FPT]
tags: [safe exam]     # TAG names should always be lowercase
---
# BY PASS SAFE EXAM
trick lỏ cho ae bypass phần mềm này
# SEB Bypass Patch v3.3.2
https://github.com/nnatun03/safe-exam-browser-bypass/blob/main/SafeExamBrowser.Monitoring.dll
https://github.com/nnatun03/safe-exam-browser-bypass/blob/main/SafeExamBrowser.SystemComponents.dll

Tải 2 bản này và mọi người cóa thể tab ra để search đáp án được nhe
## How to use

1. Tải xuống SafeExamBrowser.Monitoring.dll và SafeExamBrowser.SystemComponents.dll
2. Sao chép hai tệp này.
3. Đi đến `C:\Program Files\SafeExamBrowser\Application`.
4. Dán chúng vào thư mục này.
5. Bạn sẽ cần `quyền admin` để thay thế các tệp trong thư mục này.
6. Sau khi thay thế, mở SEB chạy trong VM.

## Recommended

Nên chỉnh cho VM trông giống như máy tính thực bằng cách sao chép mẫu và công ty của máy tính chủ (máy tính mà VM đang chạy).

**Các bước để thực hiện:**

1. Đầu tiên, đi đến thư mục nơi bạn cài đặt Windows VM. Theo mặc định, đó là thư mục *Documents*.
2. Trong thư mục *Documents*, sẽ có một thư mục có tên *Virtual Machines*.
3. Mở thư mục đó và chọn thư mục Windows VM rồi mở nó.
4. Bây giờ sẽ có một tệp với phần mở rộng `.vmx`. Nhấp chuột phải vào tệp đó và mở bằng Notepad.
5. Bây giờ dán `smbios.reflecthost = "TRUE"` vào một dòng mới như thế này:
6. nó sẽ như lày:

![https://user-images.githubusercontent.com/34748927/167270852-36b89b22-bb09-4633-9040-90bc29e64f75.png](https://user-images.githubusercontent.com/34748927/167270852-36b89b22-bb09-4633-9040-90bc29e64f75.png)

Không quan trọng nơi dán, chỉ cần dán vào một dòng mới.

## **DON'T FORGET**

Đừng quên chỉnh sửa nhật ký nếu thầy  bạn yêu cầu xem Nhật ký Máy khách và Nhật ký Chạy của bạn.

Đường dẫn nhật ký: `C:\Users\<username>\AppData\Local\SafeExamBrowser` và thay tên người dùng của bạn thay cho `<username>`

1. Trong **Runtime.log** file,
    
    ```
     INFO: [DisplayMonitor] Detected 0 active displays, 1 are allowed.
    
    ```
    

sửa thành

```
    INFO: [DisplayMonitor] Detected 1 active displays, 1 are allowed.

```

1. Trong **Client.log** file,
    
    ```
     INFO: [WirelessAdapter] Wireless networks cannot be monitored, as there is no hardware adapter available or it is turned off.
    
    ```
    

sửa thành

```
    INFO: [WirelessAdapter] Started monitoring the wireless network adapter.

```

## Làm theo các bước sau nếu bạn đang sử dụng SEB phiên bản 2.4

Các tệp `.dll` này không có trong phiên bản cũ, tức là SEB phiên bản 2.4.

Về cơ bản phiên bản SEB này không kiểm tra xem bạn có đang sử dụng VM hay không. Vì vậy việc sử dụng nó khá dễ.

Nhưng nếu thầy yêu cầu xem nhật ký, bạn cần xóa các dòng sau khỏi tệp nhật ký 
[Đường dẫn nhật ký: `C:\Users\<username>\AppData\Roaming\SafeExamBrowser` và thay tên người dùng của bạn thay cho `<username>`]:

1. Mở **Sebclient.log**
2. Bây giờ nhấn phím Ctrl và phím F.
3. Bây giờ dán `vm3dservice` vào đó và nhấp Tìm.
4. Bây giờ xóa các dòng mà thứ này được hiển thị.
5. Làm tương tự cho `VGAuthService` và `vmtoolsd` và xóa những dòng đó.

CHỈ ÁP DỤNG CHO VMWARE NHÁ !!
