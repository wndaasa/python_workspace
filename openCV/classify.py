import sys
import cv2

filename = ".\\openCV\\space_shuttle.jpg"

if len(sys.argv) > 1:
    filename = sys.argv[1]
    
img = cv2.imread(filename)

model = "googlenet/bvlc_googlenet.caffemodel"
config = 'googlenet/deploy.prototxt'

net = cv2.dnn.readNet(model, config)

classNames = None

with open('classification_classes_ILSVRC2012.txt', 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
