---
title: Write-Up MetaRed CTF 2023 - Stage 3
date: 2023-11-7 7:55:00 +0700
categories: [CTF, MetaRed-CTF-2023, Write-Up]
tags: [web, write-up, ctf]     # TAG names should always be lowercase
---
# MetaRed CTF 2023 - Stage 3

# Master JWT

[MetaRed CTF 2023 - Master JWT · Neaje]

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 3/Untitled.png">
# Baby seek and real seek

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 3/Untitled 1.png">

# Mienteles

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 3/Untitled 2.png">

# Extracttheflag!

<img src="/assets/writeup/cookie/MetaRed CTF 2023 - Stage 3/Untitled 3.png">

`Content-Type: application/x-www-form-urlencoded :` Cho biết định dạng content được gửi lên là www-form-urlencoded

Nếu không có header này, server sẽ không hiểu được rằng `_SESSION[admin]=true` là một params url encoded, và sẽ không thể parse ra key và value để set session `admin=true.`

Bài này yêu cầu bypass authentication bằng cách set giá trị admin trong session. Cần thêm `content-type` để server hiểu được dữ liệu gửi lên.
