FROM node:latest

RUN npm install -g @angular/cli

WORKDIR /var/www/html/express
RUN npm install
EXPOSE 9090

WORKDIR /var/www/html/angular
RUN npm install
EXPOSE 9091

WORKDIR /var/www/html/angular_js
RUN npm install
EXPOSE 9092

WORKDIR /var/www/html/vue_js
RUN npm install
EXPOSE 9093

ENTRYPOINT ["tail", "-f", "/dev/null"]