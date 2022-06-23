#!/bin/bash 
tar_path="chatbot-image.tar.gz"
# 导入镜像
docker load < ${tar_path} &&
# 运行镜像
image_name=`docker images|grep chatbot|cut -d" " -f1`
image_tag=`docker images|grep chatbot|cut -d" " -f4`
docker run -d ${image_name}:${image_tag} /bin/bash &&
# 拷贝项目到容器
container_name=`docker ps|grep chatbot|cut -d" " -f24`
docker cp ../BlackManba-ChatBot ${container_name}:/root &&
docker stop ${container_name} &&
# commit新镜像
docker commit ${container_name} chatbot-image:latest
# save tar
docker save -o chatbot-image.tar.gz chatbot-image-latest.tar.gz
echo "build succses"
