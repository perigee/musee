#FROM python:3.7.2-alpine3.7
FROM python:3.6-jessie


ENV USER_UID ${LOCAL_UID:-1000}


ADD requirements.txt /tmp/requirements.txt
RUN /usr/sbin/adduser --system --uid ${USER_UID} mldev


RUN pip install -r /tmp/requirements.txt
    


USER mldev
WORKDIR /home/mldev


EXPOSE 8888

#ENTRYPOINT [] https://github.com/krallin/tini
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]
