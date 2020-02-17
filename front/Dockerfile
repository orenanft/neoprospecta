FROM node:12
RUN mkdir /usr/src/app
WORKDIR /usr/src/app
RUN npm config set unsafe-perm true
RUN npm install -g @angular/cli npm-snapshot
RUN npm cache clean --force
COPY . .
