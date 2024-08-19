# we can try to replace this with alpine
FROM ubuntu:20.04
# use default answer for all prompts
ENV DEBIAN_FRONTEND=noninteractive

# python
RUN apt update && \
    apt install -y python3 python3-pip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# entry point to bash
ENTRYPOINT ["/bin/bash"]