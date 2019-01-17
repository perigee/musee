#FROM python:3.7.2-alpine3.7
FROM python:3.6-jessie


ENV USER_UID ${LOCAL_UID:-1000}


#RUN /usr/sbin/adduser -S -D -u ${USER_UID} mldev
RUN /usr/sbin/adduser --system --uid ${USER_UID} mldev


RUN pip install -U \
    #ipython==6.2.1 \
    jupyter-client==5.2.2 \
    jupyter-core==4.4.0 \
    matplotlib==2.1.2 \
    notebook==5.3.1 \
    numpy==1.14.0 \
    pandas==0.22.0 \
    scikit-learn==0.19.1 \
    scipy==1.0.0
    


USER mldev
WORKDIR /home/mldev


EXPOSE 8888

#ENTRYPOINT [] https://github.com/krallin/tini
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--NotebookApp.token=''"]
