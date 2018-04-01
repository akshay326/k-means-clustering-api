import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torch.autograd import Variable


class Img2Vec:

    # Removed CUDA support
    def __init__(self, model='resnet-18', layer='default', layer_output_size=512):
        """ Img2Vec
        :param model: String name of requested model
        :param layer: String or Int depending on model.  See more docs: https://github.com/christiansafka/img2vec.git
        :param layer_output_size: Int depicting the output size of the requested layer
        """
        self.layer_output_size = layer_output_size
        self.model, self.extraction_layer = self._get_model_and_layer(model, layer)

        self.model.eval()

        self.scaler = transforms.Scale((224, 224))
        self.normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                              std=[0.229, 0.224, 0.225])
        self.to_tensor = transforms.ToTensor()

    # Removed tensor support
    def get_vec(self, img):
        """ Get vector embedding from PIL image
        :param img: PIL Image
        :returns: Numpy ndarray
        """

        image = Variable(self.normalize(self.to_tensor(self.scaler(img))).unsqueeze(0))

        my_embedding = torch.zeros(self.layer_output_size)

        def copy_data(m, i, o):
            my_embedding.copy_(o.data)

        h = self.extraction_layer.register_forward_hook(copy_data)
        h_x = self.model(image)
        h.remove()

        return my_embedding.numpy()

    def _get_model_and_layer(self, model_name, layer):
        """ Internal method for getting layer from model
        :param model_name: model name such as 'resnet-18'
        :param layer: layer as a string for resnet-18 or int for alexnet
        :returns: pytorch model, selected layer
        """
        if model_name == 'resnet-18':
            model = models.resnet18(pretrained=True)
            if layer == 'default':
                layer = model._modules.get('avgpool')
                self.layer_output_size = 512
            else:
                layer = model._modules.get(layer)

            return model, layer

        elif model_name == 'alexnet':
            model = models.alexnet(pretrained=True)
            if layer == 'default':
                layer = model.classifier[-2]
                self.layer_output_size = 4096
            else:
                layer = model.classifier[-layer]

            return model, layer

        else:
            raise KeyError('Model %s was not found' % model_name)
