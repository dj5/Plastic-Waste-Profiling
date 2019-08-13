
import keras

import keras.layers as layers
import keras.models as models

def residual_block(input_tensor,filters, _strides=(2,2),shortcut=0):
  fil1,fil2,fil3= filters
  x= layers.Convolution2D(fil1, kernel_size=(1,1) , strides= _strides, trainable=True)(input_tensor)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  
  x= layers.Convolution2D(fil2, kernel_size=(3,3),padding='same', strides=_strides, trainable=True )(x)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  
  x= layers.Convolution2D(fil3, kernel_size=(1,1), strides=_strides, trainable=True)(x)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  
  #if shortcut==1 :
  #  short= layers.Convolution2D(fil3, kernel_size=(1,1), strides= _strides)(input_tensor)
   # short= layers.BatchNormalization(axis=3)(short)
    #x= layers.add([x,short])
    #x = layers.Activation('relu')(x)
  
  return x
def conv_block(input_tensor,filters, _strides=(2,2),shortcut=0):
  fil1,fil2,fil3= filters
  x= layers.Convolution2D(fil1, kernel_size=(1,1) , strides= _strides, trainable=True)(input_tensor)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  
  x= layers.Convolution2D(fil2, kernel_size=(3,3), strides=_strides,padding='same' , trainable=True )(x)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  
  x= layers.Convolution2D(fil3, kernel_size=(1,1), strides=_strides, trainable=True)(x)
  x= layers.BatchNormalization(axis=3)(x)
  x = layers.Activation('relu')(x)
  short= layers.Convolution2D(fil3, kernel_size=(1,1), strides= _strides, trainable=True)(input_tensor)
  short= layers.BatchNormalization(axis=3)(short)
  x= layers.add([x,short])
  x = layers.Activation('relu')(x)
  
  return x



def ResNet(input_tensor):

  x = layers.ZeroPadding2D((3, 3))(input_tensor)
  #conv1
  x= layers.Convolution2D(64, kernel_size=(7,7), strides=(2,2), trainable=True)(input_tensor)
  x= layers.BatchNormalization(axis=3)(x)
  
  x = layers.Activation('relu')(x)
  x= layers.MaxPool2D( pool_size=(3,3), strides=(2,2))(x)
  #conv2
  
  x= conv_block(x,[64,64,256],_strides=(1,1), shortcut=1)
  x= residual_block(x,[64,64,256])
  x= residual_block(x,[64,64,256])
  
  #conv3
  x= conv_block(x,[128,128,512], shortcut=1)
  x= residual_block(x,[128,128,512])
  x= residual_block(x,[128,128,512])
  x= residual_block(x,[128,128,512])
  
  #conv4
  x= conv_block(x,[256,256,1024], shortcut=1)
  x= residual_block(x,[256,256,1024])
  x= residual_block(x,[256,256,1024])
  x= residual_block(x,[256,256,1024])
  x= residual_block(x,[256,256,1024])
  x= residual_block(x,[256,256,1024])
  
  #conv5
  #x= residual_block(x,[512,512,2048],_strides=(1,1), shortcut=1)
  #x= residual_block(x,[512,512,2048])
  #x= residual_block(x,[512,512,2048])
  
  
  #x= layers.GlobalAveragePooling2D()(x)
  #x= layers.Dense(1,layers.Activation="softmax")(x)
  #model = models.Model(inputs=input_tensor, outputs=x)
  #print(model.output)
  print(x)
  return x


