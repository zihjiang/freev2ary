FROM python:2
WORKDIR /opt/v2ary
# 定时执行时间, 默认3600秒
ENV TIME=3600
# 生成文件位置
ENV TARGET=config/config.json
# 模版位置
ENV TEMPLATE=template.json
COPY requirements.txt ./
COPY freev2ary.py ./
COPY template.json ./
RUN mkdir -p config
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "./freev2ary.py" ]
