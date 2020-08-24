FROM continuumio/miniconda3
ADD . /app
WORKDIR /app
RUN conda env create -f environment.yml
# Pull the environment name out of the environment.yml
RUN echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
ENV PATH /opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH

ENTRYPOINT ["conda", "run", "-n", "djangoenv", "python", "manage.py", "runserver", "0.0.0.0:8000"]
