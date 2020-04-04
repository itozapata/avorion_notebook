FROM continuumio/miniconda3

ADD environment.yml /tmp/environment.yml
RUN conda env update -n base -f /tmp/environment.yml

# SHELL ["conda", "run", "-n", "dash", "/bin/bash", "-c"]
run pip install dash==1.10.0

COPY . /usr/app
WORKDIR /usr/app

EXPOSE 80

CMD python server.py
