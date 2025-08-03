# 音訊轉檔 GUI 工具

本工具可將各種音訊格式（MP3, WAV, M4A, FLAC 等）轉換為：

- WAV (48000Hz, 24bit 無損音質)
- MP3 (320kbps 高音質)

## 功能特色

- 拖曳加入檔案
- 支援多檔批次轉換
- 可自訂輸出資料夾
- 顯示進度條與轉換紀錄
- 可打包為 Windows `.exe` 執行檔

## 執行方式

1. 安裝 Python 3.13.5 與 FFmpeg
2. 執行：
   ```
   python main.py
   ```

## 打包方式

使用 pyinstaller：

```
pyinstaller main.py --onefile --noconsole --icon=assets/icon.ico
```

## 直接使用

[EXE](/dist/main.exe)

## 參考解決問題

[ffmpeg command problem in python to remove silences at the beggining and end. error: returned non-zero exit status 4294967274](https://stackoverflow.com/questions/78937907/ffmpeg-command-problem-in-python-to-remove-silences-at-the-beggining-and-end-er)
