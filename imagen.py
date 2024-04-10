import cv2 #descargar el paquete de opencv2
imagen = cv2.imread("images.jfif",1)# cambiar el valor entero por 0 para cambiar color
cv2.imshow('paisaje',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()