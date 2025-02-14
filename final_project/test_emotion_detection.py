
from  emotion_detection.emotion_detection import emotion_detector
import unittest


result1 = emotion_detector('I am glad this happaned')

self.assertEqual(result1['label'], 'joy')

result2 = emotion_detector('I am really mad about this')

self.assertEqual(result2['label2'], 'anger')

result3 = emotion_detector('I am disgusted hearing about this')

self.assertEqual(result3['label3'], 'disgust')

result4 = emotion_detector('I am so sad about this')

self.assertEqual(result4(['label4'], 'sadness'))

result5= emotion_detector('I am really afraid that this will happen again')

self.assertEqual(result5['label5'], 'fear')


unittest.main()