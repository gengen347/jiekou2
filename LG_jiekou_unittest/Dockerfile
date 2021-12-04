FROM python:3.8
ADD jdk8.gz /usr/local
ENV JAVA_HOME /usr/local/jdk1.8.0_11
WORKDIR /auto
ADD . /auto
RUN pip install -r ku.txt -i https://pypi.douban.com/simple