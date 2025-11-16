FROM ozkrelo/x_mobipick_labs:noetic-v1.1

# remove old /entrypoint.sh to avoid confusion
RUN rm -f /entrypoint.sh

# Inherit host user/uid/gid via build args
ARG USER
ARG UID
ARG GID

# Make USER and HOME available at run time
ENV USER=${USER} \
    HOME=/home/${USER}

# Create group and user matching host UID/GID
RUN set -eux; \
    : "${USER:?USER build-arg required}"; \
    : "${UID:?UID build-arg required}"; \
    : "${GID:?GID build-arg required}"; \
    if ! getent group "${GID}" >/dev/null 2>&1; then \
        groupadd -g "${GID}" "${USER}"; \
    fi; \
    if ! id -u "${USER}" >/dev/null 2>&1; then \
        useradd -m -u "${UID}" -g "${GID}" -s /bin/bash "${USER}"; \
    fi

# Install sudo and allow the user to use it without password inside the container
RUN apt-get update && \
    apt-get install -y sudo && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" > "/etc/sudoers.d/${USER}" && \
    chmod 0440 "/etc/sudoers.d/${USER}"

# From here on, build steps run as the non-root user
USER ${USER}
WORKDIR ${HOME}

# Copy custom entrypoint for non-root user; assume it's executable on host
COPY entrypoint_user.sh /usr/local/bin/entrypoint_user.sh

# Fetch helper scripts into $HOME and enable them from the user's bash profile
RUN set -eux; \
    cd "${HOME}"; \
    if [ ! -d scripts ]; then \
        git clone https://github.com/oscar-lima/mobipick_labs_scripts.git scripts; \
    fi; \
    printf '\n# personal config starts here\nsource ${HOME}/scripts/permanent.sh\n' \
      >> ${HOME}/.bashrc; \
    install -d "${HOME}/scripts/personal_config"; \
    cp -a "${HOME}/scripts/others/personal_config_example/." \
      "${HOME}/scripts/personal_config/"

ENTRYPOINT ["/usr/local/bin/entrypoint_user.sh"]
CMD ["bash"]
