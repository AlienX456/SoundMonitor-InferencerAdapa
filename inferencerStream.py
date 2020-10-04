from kafka import KafkaConsumer
import io
import soundfile as sf
from inferencer.Adapatask5 import DcaseAdapatask5
from resources.awsS3Resource import AwsS3Resource
import logging
logging.getLogger().setLevel(logging.INFO)

inferencer = DcaseAdapatask5()

awsS3 = AwsS3Resource()

consumer = KafkaConsumer('audio-upload-event',
                         group_id='inferencer-group',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest')


for message in consumer:
    fileName = message.value.decode('utf-8')
    logging.info("New Audio arrived ID {}".format(fileName))
    try:
        data, samplerate = sf.read(io.BytesIO(awsS3.getStreamData(fileName)))
        result = inferencer.runInferencer(data, samplerate)
        logging.info("Processing Finished for {}".format(fileName))
        print(result)
    except Exception as e:
        logging.error('There was an error while Processing : {}'.format(str(e)))