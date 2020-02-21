FROM python:alpine
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update && \
    apk upgrade --no-cache && \
    apk add --no-cache \
        gcc \
        g++ \
        ca-certificates \
        # libffi-devel \
        # openssl-devel \
        libc-dev \
        git \
        sqlite && \
    update-ca-certificates
RUN git config --global http.sslVerify false
# RUN pip install --upgrade --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org pip setuptools wheel && \
#     pip install --upgrade --trusted-host=pypi.org --trusted-host=pypi.python.org --trusted-host=files.pythonhosted.org \
#     poetry django djangorestframework django-cors-headers django-extensions django-environ orator \
#     pylint pyformat flake8 bpython

WORKDIR /home/www
