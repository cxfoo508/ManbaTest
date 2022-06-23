FROM python:3.7.9
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /BlackManba-ChatBot
RUN pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com pipenv
COPY . /BlackManba-ChatBot/
RUN pipenv install --system 
ENTRYPOINT ["python", "run.py"]