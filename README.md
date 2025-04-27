
# Pi Meeting Screen

Two React applications to be ran on a Pi with a screen & another computer. The computer application will allow you to send messages to the Pi which will make the Pi UI reflect the status you sent it (i.e. "In a Meeting!" or "Video is On!").

## But Why?

I've been working from home since Covid times but rarely went on camera unless asked to. As my responsibilities shifted, I found myself working at weird times, attending meetings randomly, and (as my team expanded) having a lot of interviews at random times.

My wife generally understands my schedule and when I have meetings and when I'll be on camera so that she doesn't accidentally barge into my office.

She's the greatest woman in the world. She was bringing me a sandwich and some snacks while I was on camera for an interview.

No one really cares if she walks in the background of the video, of course -- I think we all understand that things like this happen when you're working from home. I did, however, want to make some way for her to know when I'm in a meeting without having to:

1. Text her
2. Leave a physical note on my door
3. Make her check my calendar

I took my Raspberry Pi 4B (which she got me for my birthday two months after we started dating in 2020 (I told you she was the best)), bought a 5" screen for it, and 3D printed a tiny enclosure for it. Now this sits upstairs with the rest of the smart home nonsense so she can easily see what I'm up to in my office without having to walk all the way downstairs or risk being caught on camera.

## Requirements

- A Raspberry Pi for the `Host` application
  - _My Setup: [Raspberry Pi 4B 4GB RAM](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X?crid=1FH0GZD1GG510&dib=eyJ2IjoiMSJ9.ap3wq-hWBrbjbxnXaSLJziwQIAbyxiVeBRjaZyOzDpgfdTS4pr_55N4uBsdWFVWPAzPFDxep03wCpdTpyF15OyfLlxgriRhO-BdMSO1GUAdxq6mELO6qYH0dNzBcNB-ql-nmGzBj0po4hc2HRdJxjhvD8DEpM9z93s6K4wFAHkjxQEpyS_nV6nTYE2MuqhuAeJWu4yrBMySON-qLMi7XTpF7Uni6WPZAnVzw_8hCbyo.E2-FR4-gxkOng3FFdwhLD6bJx5O5qHSviENmi0Z_8eI&dib_tag=se&keywords=raspberry%2Bpi%2B4b&qid=1745768546&sprefix=raspberry%2Bpi%2B4b%2Caps%2C228&sr=8-4&th=1)_
- Some display for the Pi
  - _My Setup: [ELECROW 5" Screen](https://www.amazon.com/ELECROW-Touchscreen-Resolution-Resistive-Compatible/dp/B013JECYF2?crid=1ON76IXG52WB6&dib=eyJ2IjoiMSJ9.17ydnxKPkBISj6Ift_LRfSbS_9nNuVTODksJXNUqTKRJC4M7ZJPrnOYx7AGdRY5jq-dpxunAj6RvFvJaUBaUKtmUwZZXyX88uvlDHu94I-ljjzfFfYdBDNJxBMRshSpS6ejczfZkSa_EsmqPEYzOLZv_TP1IXwSwGXfyRGIZl5OHD5J3cksHOMQoIK_KiEaiLevfMKCKxNq0ENRMdaJWmc1XmYR9NP4M7Pp76BK2FgmMaqHuwjgAu8L7MnR3_Cqaeu4Qt08sRli2z-xe-5m_dLtcj4dkDCB3xTTowrkz61c.4PLhj9s4mJ3u7MH9ZIuAbeCHC-UEHmzbUJnAhbZOT7I&dib_tag=se&keywords=elecrow+5%22+pi+screen&qid=1745768658&s=electronics&sprefix=elecrow+5+pi+scree%2Celectronics%2C112&sr=1-3)_
  - _If I could do it again, I think I'd choose a different brand since I couldn't get the touchscreen to work very well and have to keep fiddling with the resolution on this screen... I've had better success with [this 7" screen](https://www.amazon.com/Lebula-Touchscreen-Raspberry-1024X600-Capacitive/dp/B07VNX4ZWY?crid=1AMLSXNMMBW97&dib=eyJ2IjoiMSJ9.bFAo-rN29W5g36YBnBXuxnSYcSfaJXghGFFtHgnipJjZSYoC6V3ft0rIGMSZ9cXqMtMsC2hWySutaV5C8nIx6ios9b5SYU3N4iQCWANepE8M0yKoNUabiF5OlZjGryywG3y3yHYrg6LtOXseVXtzRaBlyF5Hsz1e5EY4NPX1Eq5TXtxW0o-ORQPo7LC-QuTvQhQnQKS1tZ1osGmhFFHUjGM47DST4I1X7J1pQPyP4f2g5a5kfN16IuWKyx406NdsTnB5bO-pdANmAS5BOOL0uPvGHzjeuNW7V9UmFxiytsI.-OK2zheZpzXiq9z51Qgn2-obxjuv14MkoE5DODF3cEw&dib_tag=se&keywords=ROADOM%2B7%E2%80%99%E2%80%99%2BRaspberry%2BPi%2BScreen%2C&qid=1745768739&s=electronics&sprefix=roadom%2B7%2Braspberry%2Bpi%2Bscreen%2C%2Celectronics%2C103&sr=1-3&th=1)_
- A computer to run the `Client` application
- `Node v???`
- `npm v???`

## Running on the Pi

## Running on a Computer
