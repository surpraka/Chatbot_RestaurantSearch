from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput
import ruamel.yaml
import warnings
warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxb-1352818846263-1352865282439-K9vQrtsL6uz3EkWfrWfP3Z7v', #app verification token
                            'xoxp-1352818846263-1360827572182-1367604602082-5e1974b93304d9cfd71b186c7561a167', # bot verification token
							'NyYvmOGM6XiI6QbzYMjZDXxU', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))