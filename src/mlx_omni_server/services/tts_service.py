from pathlib import Path

from f5_tts_mlx.generate import generate

from ..models.tts import AudioFormat


class F5Model():

    def __init__(self):
        pass

    def generate(self, text: str, speed, output_path):
        generate(
            generation_text=text,
            speed=speed,
            output_path=output_path,
        )


class TTSService:
    model: F5Model

    def __init__(self):
        self.model = F5Model()
        # 直接指定本地音频文件路径
        self.sample_audio_path = Path("sample.wav")

    async def generate_speech(
        self,
        model: str,
        input_text: str,
        voice: str,
        response_format: AudioFormat = AudioFormat.WAV,
        speed: float = 1.0
    ) -> bytes:
        """
        Generate speech from text.

        Args:
            model: The TTS model to use
            input_text: The text to convert to speech
            voice: The voice to use
            response_format: The audio format to generate
            speed: The speed of the generated audio

        Returns:
            bytes: The generated audio content
        """

        try:
            self.model.generate(text=input_text, speed=speed, output_path=self.sample_audio_path)
            with open(self.sample_audio_path, 'rb') as audio_file:
                audio_content = audio_file.read()
            self.sample_audio_path.unlink(missing_ok=True)
            return audio_content
        except Exception as e:
            raise Exception(f"Error reading audio file: {str(e)}")
