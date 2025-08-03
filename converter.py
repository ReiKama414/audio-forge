import subprocess
import os

def convert_audio_files(input_paths, output_format="wav", output_dir=None, log_callback=None):
    output_args = {
        "wav": ["-ar", "48000", "-ac", "2", "-sample_fmt", "s16"],
        "mp3": ["-b:a", "320k"],
    }

    for input_path in input_paths:
        filename = os.path.splitext(os.path.basename(input_path))[0]
        ext = output_format.lower()
        output_dir = output_dir or os.path.dirname(input_path)
        output_path = os.path.join(output_dir, f"{filename}.{ext}")
        
        # 輸出先到暫存檔，避免 ffmpeg 嘗試覆蓋源檔失敗
        temp_output = os.path.join(output_dir, f"{filename}_temp.{ext}")
        args = ["ffmpeg", "-y", "-i", input_path, *output_args[ext], temp_output]

        result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
        if result.returncode == 0:
            os.replace(temp_output, output_path)
            if log_callback:
                log_callback(f"已轉: {input_path} → {output_path}")
        else:
            if "Invalid data found" in result.stderr or "Failed to find two consecutive MPEG" in result.stderr:
                if log_callback:
                    log_callback(f"轉換失敗（格式錯誤或損壞）: {input_path}")
                raise RuntimeError(f"輸入檔案可能損壞或不是有效音訊格式：{input_path}")
            else:
                if log_callback:
                    log_callback(f"轉換失敗: {input_path}\n{result.stderr}")
