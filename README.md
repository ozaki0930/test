# 音声周波数ビジュアライザー

このリポジトリには、マイクから入力された音声をリアルタイムで周波数表示する `audio_visualizer.py` が含まれています。

## 使い方

1. 依存関係のインストール（Python3 が必要です）
   ```bash
   pip install sounddevice matplotlib numpy
   ```
2. スクリプトの実行
   ```bash
   python3 audio_visualizer.py
   ```
   実行すると新しいウィンドウが開き、リアルタイムで周波数スペクトルが表示されます。

マイク入力が利用できない環境では動作しない場合があります。
