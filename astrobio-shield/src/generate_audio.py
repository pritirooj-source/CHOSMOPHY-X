import os
import wave
import math
import struct

def create_distinct_scifi_audio():
    audio_dir = os.path.join("assets", "audio")
    os.makedirs(audio_dir, exist_ok=True)
    
    sample_rate = 22050
    
    # 1. Telemetry Click / UI Navigation (Crisp double-tech blip)
    click_path = os.path.join(audio_dir, "telemetry_click.wav")
    with wave.open(click_path, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        duration = 0.06
        frames = int(sample_rate * duration)
        for i in range(frames):
            t = i / sample_rate
            val = int(8000 * (math.sin(2 * math.pi * 1800 * t) + 0.5 * math.sin(2 * math.pi * 3600 * t)) * math.exp(-t * 30))
            f.writeframes(struct.pack('<h', val))

    # 2. Execute Simulation (Deep Star-Trek style command confirmation sweep)
    alert_path = os.path.join(audio_dir, "red_alert.wav")
    with wave.open(alert_path, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        duration = 0.45
        frames = int(sample_rate * duration)
        for i in range(frames):
            t = i / sample_rate
            freq = 440 + 440 * (t / duration) # Frequency sweep upwards
            val = int(12000 * math.sin(2 * math.pi * freq * t) * math.exp(-t * 4))
            f.writeframes(struct.pack('<h', val))

    # 3. Export PDF & Sync (Magical futuristic data-lock chime)
    shield_path = os.path.join(audio_dir, "shield_activation.wav")
    with wave.open(shield_path, 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(sample_rate)
        duration = 0.55
        frames = int(sample_rate * duration)
        for i in range(frames):
            t = i / sample_rate
            val = int(10000 * (math.sin(2 * math.pi * 880 * t) + math.sin(2 * math.pi * 1320 * t)) / 2 * math.exp(-t * 5))
            f.writeframes(struct.pack('<h', val))
            
    print("✨ Success! Distinct Sci-Fi audio assets generated inside 'assets/audio/' folder!")

if __name__ == "__main__":
    create_distinct_scifi_audio()