FROM kspckan/netkan
USER root
RUN python3 -m pip install --upgrade pip
ADD . /workdir
WORKDIR /workdir
RUN pip install .
WORKDIR /
RUN rm -r /workdir
ENTRYPOINT ["inflate-netkan"]
