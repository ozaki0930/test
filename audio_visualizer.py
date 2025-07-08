#!/usr/bin/env python3
"""音声の周波数をリアルタイムでビジュアライズする簡単なスクリプト"""

import queue
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

SAMPLE_RATE = 44100  # サンプリング周波数
BLOCK_SIZE = 1024

q = queue.Queue()


def audio_callback(indata, frames, time, status):
    """オーディオ入力からデータをキューへ入れるコールバック"""
    if status:
        print(status)
    q.put(indata.copy())


def update(frame):
    """アニメーション更新用の関数"""
    while not q.empty():
        data = q.get()
        spectrum = np.abs(np.fft.rfft(data[:, 0]))
        line.set_ydata(spectrum)
    return line,


fig, ax = plt.subplots()

freqs = np.fft.rfftfreq(BLOCK_SIZE, 1 / SAMPLE_RATE)
line, = ax.plot(freqs, np.zeros_like(freqs))
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('Amplitude')
ax.set_ylim(0, 50)
ax.set_xlim(0, SAMPLE_RATE / 2)


if __name__ == '__main__':
    stream = sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
    )
    with stream:
        ani = FuncAnimation(fig, update, interval=30, blit=True)
        plt.show()
