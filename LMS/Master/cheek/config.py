import json
import pathlib

project_root = pathlib.Path(__file__).parent.parent
config_file = project_root / 'config.json'

with open(config_file) as file:
    __config = json.dumps(json.load(file))


__config = __config.replace('${PROJECT_ROOT}', str(project_root.absolute()))
__config = json.loads(__config)
__javascript_file = __config['xpathFile']

with open(__javascript_file) as file:
    JAVASCRIPT_TO_EXECUTE = file.read()

EXECUTABLE = __config['path']
DATA_FILE = __config['dataFile']
DOCX_FILE = __config['docxFile']
QUESTION = __config['question']
CHECKBOXES = __config['checkBoxes']
SOLUTION = __config['solution']
OPTIONS = __config['options']
ADD_OPTION = __config['addOption']
ADD_BUTTON = __config['addButton']
CLOSE_BUTTON = __config['closeButton']
SAVE_BUTTON = __config['saveButton']
HINDI_QUESTION = __config['hindiquestion']
HINDI_SOLUTION = __config['hindisolution']
HINDI_OPTIONS = __config['hindioptions']
