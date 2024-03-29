import unittest
from inferencer.adapa_task5 import DcaseAdapatask5
import soundfile as sf
import io


class TestStringMethods(unittest.TestCase):

    def test_inferencer(self):
        inferencer = DcaseAdapatask5()
        with open('test/test_audio.wav', 'rb') as audio:
            data, samplerate = sf.read(io.BytesIO(audio.read()))
        result = inferencer.run_inferencer("", data, samplerate)

        result_expected_keys = ['audio_filename', '1-1_small-sounding-engine',
          '1-2_medium-sounding-engine', '1-3_large-sounding-engine',
          '1-X_engine-of-uncertain-size', '2-1_rock-drill', '2-2_jackhammer',
          '2-3_hoe-ram', '2-4_pile-driver', '2-X_other-unknown-impact-machinery',
          '3-1_non-machinery-impact', '4-1_chainsaw',
          '4-2_small-medium-rotating-saw', '4-3_large-rotating-saw',
          '4-X_other-unknown-powered-saw', '5-1_car-horn', '5-2_car-alarm',
          '5-3_siren', '5-4_reverse-beeper', '5-X_other-unknown-alert-signal',
          '6-1_stationary-music', '6-2_mobile-music', '6-3_ice-cream-truck',
          '6-X_music-from-uncertain-source', '7-1_person-or-small-group-talking',
          '7-2_person-or-small-group-shouting', '7-3_large-crowd',
          '7-4_amplified-speech', '7-X_other-unknown-human-voice',
          '8-1_dog-barking-whining', '1_engine', '2_machinery-impact',
          '3_non-machinery-impact', '4_powered-saw', '5_alert-signal', '6_music',
          '7_human-voice', '8_dog']
        self.assertEqual(result.keys().tolist(), result_expected_keys)


if __name__ == '__main__':
    unittest.main()