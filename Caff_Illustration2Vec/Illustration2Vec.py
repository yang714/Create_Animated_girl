import i2v
from PIL import Image
import  caffe

illust2vec = i2v.make_i2v_with_chainer(
    "C:/Users\PC\PycharmProjects\Caff_Illustration2Vec/illust2vec_tag_ver200.caffemodel", "C:/Users\PC\PycharmProjects\Caff_Illustration2Vec/tag_list.json")

def filter(path):
    img = Image.open(path)
    b = illust2vec.estimate_specific_tags([img], ["1girl"])
    if (b[0]['1girl']) > 0.85:
        return  True
    else:
        return False

