FROM node:latest

ARG APPLICATION_DIRECTORY=/app

RUN npm install -g @vue/cli && \
    npm install -g @vue/cli-service-global

WORKDIR ${APPLICATION_DIRECTORY}

VOLUME ${APPLICATION_DIRECTORY}

EXPOSE 8000
EXPOSE 8080

CMD ["npm", "run", "serve"]
